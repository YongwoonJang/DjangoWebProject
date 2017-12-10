from django.shortcuts import render
from .models import Content, Service
from .forms import SourceForm
import logging
from django.http import HttpResponseRedirect
from django.core.files import File

# Create your views here.
def index(request):

    logger = logging.getLogger(__name__)
    source_list = Content.objects.order_by('id')
    menu_list = Service.objects.order_by('id')

    logger.error('request receives')
    # view가 form으로 부터 정보를 받아서 database로 전달함.
    if request.method == "POST":

        logger.error('database saving is executing')
        form = SourceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
    else:
        form = SourceForm()

    context = {'source_list':source_list,'menu_list':menu_list, 'form':form, 'index':0}
    return render(request, 'encyclopedia/maintab.html', context)

def upload_file(request):

    logger = logging.getLogger(__name__)
    source_list = Content.objects.order_by('id')
    menu_list = Service.objects.order_by('id')

    if request.method == 'POST':
            logger.error("Uploadfileform and form. is Post is executing")
            fileform = SourceForm(request.POST)

            if(fileform.is_valid()):
                with open('C:/Users/USER/Documents/projectstarbucks/encyclopedia/static/encyclopedia/sourcestorage/hello.html', 'w+') as f:
                    myfile = File(f)
                    myfile.write('<!DOCTYPE html><html>'+'<head>'+'<style>'+fileform.cleaned_data['csscontents']+'</style>'+'</head>'+'<body>'+fileform.cleaned_data['htmlcontents']+'</body>'+'<script>'+fileform.cleaned_data['javascriptcontents']+'</script></html>')
                myfile.closed
                f.closed

    else:
        fileform = SourceForm()
        logger.error("request is not post and uploadfileform is not valid.")

    context = {'source_list':source_list,'menu_list':menu_list, 'form':fileform, 'index':1}
    return render(request, 'encyclopedia/maintab.html', context) # to do configure to current tab.
