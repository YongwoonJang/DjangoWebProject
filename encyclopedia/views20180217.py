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
from konlpy.tag import Kkma
from konlpy.utils import pprint 

import sys

# Encoding
reload(sys)
sys.setdefaultencoding('utf-8')

# String to Noun formatting
kkma = Kkma()

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
    source_list = Content.objects.filter(htmlcontents__contains=searchtext)
    context = serialize('json',source_list)

    # receving data..
    if jpype.isJVMStarted():
	jpype.attachThreadToJVM() 
    
    holyBible = open("usr/local/web/encyclopedia/dictionary/genesis1.txt", "r")
    genesisFirst = holyBible.read()
    genesisChunks = kkma.nouns(genesisFirst)
    
    logger.error("the length of genesis noun is  "+str(len(genesisChunks)))
    
    candidate = []
    for x in genesisChunks:
	if searchtext == x:
		candiate.append(x)
    
        

    # NLP
    #words = konlpy.tag.Twitter().pos(searchtext)
    #words = konlpy.tag.Twitter().pos(genesisFirst)
    #chunks = parser.parse(words)

    # Making list
    # baseConcept..(transcent, good, bad, sosos) 
    baseConcept = []
    baseConcept.append(["love",(0,3,0,0)])
    baseConcept.append(["light",(0,1,0,0)])
    baseConcept.append(["god",(1,1,0,0)])
    baseConcept.append(["heavens",(0,0,0,1)])
    baseConcept.append(["earth",(0,0,0,1)])
    
    # input attribute..(from input tab) 
    inputAttr = []
    inputAttr.append((0,0,0,0))

    # search "input word is in baseConcept" 
    for element in baseConcept:
	if element[0] == searchtext:
		inputAttr.append(element[1])

    index = 0
    selectList = [99999,"No value"]
    # select nearest word. 
    for element in baseConcept: 
	dist = np.linalg.norm(np.asarray(element[1])-np.asarray(inputAttr[0]))
	if selectList[0] > dist:
		selectList[0] = dist 
		selectList[1] = element[0]

    logger.error("The answer is ")
    logger.error(selectList[1])

    return JsonResponse(context, safe=False)

# define code page
def page(request):
    logger = logging.getLogger(__name__)
    return HttpResponseRedirect(request.path)
