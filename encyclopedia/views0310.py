# coding=UTF-8
from django.shortcuts import render
from .models import Content, Service
from .forms import SourceForm
import logging
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.serializers import serialize
from django.core.files import File

import tensorflow as tf
import numpy as np

import konlpy
import nltk
import jpype
from konlpy.tag import Twitter
from konlpy.utils import pprint 
from gensim.models import Word2Vec

import sys
import json
import io

from .sentencereader import SentenceReader

# Encoding for json and hangum input setting
reload(sys)
sys.setdefaultencoding('utf-8')

# Data sets
HANGUL_TRAINING = "hangul_training.csv"
HANGUL_TRAINING_PATH = "../testset/hangul_training.csv"

HANGUL_TEST = "hangul_test.csv"
HANGUL_TEST_PATH = "../testset/hangul_test.csv"

# Text analyzer. 
grammar = """
	NP: {<N.*>*<Suffix>?}   # Noun phrase
	VP: {<V.*>*}            # Verb phrase
	AP: {<A.*>*}            # Adjective phrase    
"""
parser = nltk.RegexpParser(grammar)

# Create your views here.
def index(request):
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    source_list = Content.objects.order_by('id')
    form = SourceForm()

    #file writing.
    for i in range(0, source_list.count()):
        with open('/usr/local/web/encyclopedia/static/encyclopedia/sourcestorage/codeinventory/'+str(source_list[i].id)+".html", 'w+') as f:
            myfile = File(f)
            myfile.write('<!DOCTYPE html><html>'+'<head>'+'<style>'+source_list[i].csscontents+'</style>'+'</head>'+'<body>'+source_list[i].htmlcontents+'</body>'+'<script>'+source_list[i].javascriptcontents+'</script></html>')
            myfile.closed
            f.closed

    #context = {'source_list':source_list,'menu_list':menu_list, 'form':form, 'index':0 }
    context = {'source_list':source_list,'menu_list':["list","insert","search"], 'form':form, 'index':0 }
    return render(request, 'encyclopedia/maintab.html', context)

# file upload.
def upload_file(request):

    logger = logging.getLogger(__name__)
    source_list = Content.objects.order_by('id')
    logger.error("this things are happen")
    if request.method == 'POST':

            logger.error("Uploadfileform and form. Post is executing")
            fileform = SourceForm(request.POST)
            logger.error(request.POST)
            if(fileform.is_valid()):
                if(request.POST['selector'] == 'makeDEMO'):
                    logger.error("makeDEMO is executing.")
                    with open('/usr/local/web/encyclopedia/static/encyclopedia/sourcestorage/hello.html', 'w+') as f:
                        myfile = File(f)
                        logger.error(fileform.cleaned_data['csscontents'])
                        myfile.write('<!DOCTYPE html><html>'+'<head>'+'<style>'+fileform.cleaned_data['csscontents']+'</style>'+'</head>'+'<body>'+fileform.cleaned_data['htmlcontents']+'</body>'+'<script>'+fileform.cleaned_data['javascriptcontents']+'</script></html>')
                        myfile.closed
                        f.closed
                    return HttpResponse("success")

                else:
                    with open('/usr/local/web/encyclopedia/static/encyclopedia/sourcestorage/codeinventory/'+str(source_list.count())+'.html', 'w+') as f:
                        myfile = File(f)
                        logger.error(fileform.cleaned_data['csscontents'])
                        myfile.write('<!DOCTYPE html><html>'+'<head>'+'<style>'+fileform.cleaned_data['csscontents']+'</style>'+'</head>'+'<body>'+fileform.cleaned_data['htmlcontents']+'</body>'+'<script>'+fileform.cleaned_data['javascriptcontents']+'</script></html>')
                        myfile.closed
                        f.closed
                    logger.error("file save is executing")
                    post = fileform.save(commit=True)
                    post.save()

    else:
        logger.error("request is not post and uploadfileform is not valid.")
        fileform = SourceForm()


    context = {'source_list':source_list,'menu_list':["list","insert","search"], 'form':fileform, 'index':0}
    return render(request, 'encyclopedia/maintab.html', context) # to do configure to current tab.

def search_data(request):
    logger = logging.getLogger(__name__)
    searchtext = request.POST.get('searchtext','')
    
    # initilize genesisChunk...
    genesisChunks = []
    candidate = []
    syntax = []   
    result = []

    # receving data..
    if jpype.isJVMStarted():
	jpype.attachThreadToJVM() 

    # model setting (아담 / Noun)     
    sentences_vocab = SentenceReader('/usr/local/web/encyclopedia/dictionary/genesis1p.txt')
    sentences_train = SentenceReader('/usr/local/web/encyclopedia/dictionary/genesis1p.txt')
    
    model = Word2Vec()
    model.build_vocab(sentences_vocab)
    model.train(sentences_train,total_examples=model.corpus_count,epochs=model.epochs)
   
    model.save('model')
    model = Word2Vec.load('model')
    
    # model setting 
    sentences_vocab = SentenceReader('/usr/local/web/encyclopedia/dictionary/genesis2p.txt')
    sentences_train = SentenceReader('/usr/local/web/encyclopedia/dictionary/genesis2p.txt')
    
    modelOne = Word2Vec()
    modelOne.build_vocab(sentences_vocab)
    modelOne.train(sentences_train,total_examples=modelOne.corpus_count,epochs=modelOne.epochs)
   
    modelOne.save('model')
    modelOne = Word2Vec.load('model')

    # search text 
    posMaker = Twitter()   
    searchMetatext = posMaker.pos(searchtext)
    
    # (아담/Noun)
    searchtextZero = str("/".join(searchMetatext[0]))
    # (Noun)
    searchtextOne  = searchMetatext[0][1]
  
    # Previously Items are attached form base / 
    # Later Items are attached from result / 
    for item in model.most_similar(positive=[searchtextZero], topn=100):
	candidate.append(item[0])

    for item in modelOne.most_similar(positive=[searchtextOne], topn=100):
	syntax.append(item[0])

    result.append(searchtext)
	    
    index = 0
    for item in candidate:
	if ((item.split("/")[1] == syntax[index])or(item.split("/")[1] == "Noun")) :
		result.append(item.split("/")[0])

    logger.error(result)
    logger.error(syntax)

    context = json.dumps(result, ensure_ascii=False)
    return JsonResponse(context, safe=False)

# define code page
def page(request):
    logger = logging.getLogger(__name__)
    return HttpResponseRedirect(request.path)

# Make check step 
# Prevent from selecting same word. 
def checkWord(start , end, step):
	while start <= end: 
		yield start 
		start += step

# Check whether candidates are duplicated. 
def checkDup(candidate, word):
    size = len(candidate)
    for i in range(0, size):
	if candidate[i] == word:
		return True
    return False

 
