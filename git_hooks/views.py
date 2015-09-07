# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from git_hooks.gitpull import GitPuller


@csrf_exempt
def git_pull(request):
    out = {}
    q = GitPuller(getattr(settings, 'GIT_PULL_BASE_DIR', settings.BASE_DIR), getattr(settings,'GIT_PULL_BRANCH',None))
    # Запускаем процесс...
    q.run()
    try:
        return render(request, 'git_pull.html', out)
    except:
        return HttpResponse(q.git_pull_output)
