from django.http import HttpResponse
from django.shortcuts import render
from .models import Project
from .models import Video

#def ret(request):
    #return HttpResponse('Hello, world')


#def base(request):
   # return render(request, 'kety.html')


def project_index(request):
    projects=Project.objects.all()
    context={
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project=Project.objects.get(pk=pk)
    context={
        'project': project
    }
    return render(request, 'project_detail.html', context)

def pro(request, pk):
    video1 = Video.objects.get(pk=pk)
    context={
        'video1': video1
    }
    return render(request, 'project_detail.html', context)



