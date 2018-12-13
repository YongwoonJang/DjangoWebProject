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
from konlpy.tag import Komoran
from konlpy.utils import pprint 

import sys
import json

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

    # receving data..
    if jpype.isJVMStarted():
	jpype.attachThreadToJVM() 
  
    with open("/usr/local/web/encyclopedia/dictionary/genesis1p.txt","r") as holyBible:
	for item in holyBible:
		item = item.strip()
		genesisChunks.append(item)
        
    candidate = []
    lenOfGenesis = len(genesisChunks)
    logger.error("the string len is "+str(lenOfGenesis))
    for x in range(0, lenOfGenesis):
	if genesisChunks[x] == searchtext:
		for i in checkWord(x,lenOfGenesis,1):
			if genesisChunks[i] != searchtext:
				if not checkDup(candidate, genesisChunks[i]):
					candidate.append(genesisChunks[i])
					break
		for i in checkWord(x,0,-1):
			if genesisChunks[i] != searchtext:
				if not checkDup(candidate, genesisChunks[i]):
					candidate.append(genesisChunks[i])
					break
		
    if len(candidate) == 0:
	candidate.append("인접한 값이 없습니다.")

    context = json.dumps(candidate, ensure_ascii=False)
    logger.error(context)
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

 
