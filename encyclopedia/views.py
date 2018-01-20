from django.shortcuts import render
from .models import Content, Service
from .forms import SourceForm
import logging
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.files import File

# Create your views here.
def index(request):

    logger = logging.getLogger(__name__)
    source_list = Content.objects.order_by('id')
    form = SourceForm()

    #file writing.
    for i in range(0, source_list.count()):
        with open('C:/Users/USER/Documents/DjangoWebProject/encyclopedia/static/encyclopedia/sourcestorage/codeinventory/'+str(i)+".html", 'w+') as f:
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

    if request.method == 'POST':

            logger.error("Uploadfileform and form. Post is executing")
            fileform = SourceForm(request.POST)
            logger.error(request.POST)
            if(fileform.is_valid()):
                if(request.POST['selector'] == 'makeDEMO'):
                    logger.error("makeDEMO is executing.")
                    with open('C:/Users/USER/Documents/DjangoWebProject/encyclopedia/static/encyclopedia/sourcestorage/hello.html', 'w+') as f:
                        myfile = File(f)
                        logger.error(fileform.cleaned_data['csscontents'])
                        myfile.write('<!DOCTYPE html><html>'+'<head>'+'<style>'+fileform.cleaned_data['csscontents']+'</style>'+'</head>'+'<body>'+fileform.cleaned_data['htmlcontents']+'</body>'+'<script>'+fileform.cleaned_data['javascriptcontents']+'</script></html>')
                        myfile.closed
                        f.closed
                    return HttpResponse("success")

                else:
                    with open('C:/Users/USER/Documents/DjangoWebProject/encyclopedia/static/encyclopedia/sourcestorage/codeinventory/'+str(source_list.count())+'.html', 'w+') as f:
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


    context = {'source_list':source_list,'menu_list':["list","insert","search"], 'form':fileform, 'index':1}
    return render(request, 'encyclopedia/maintab.html', context) # to do configure to current tab.

# define code page
def page(request):
    logger = logging.getLogger(__name__)
    return HttpResponseRedirect(request.path)
