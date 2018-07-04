from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.template import loader


# Create your views here.

def error_view(request):
    return render(request, 'accounts/error_view.html')


def csrf_error_view(request, reason="", template_name='accounts/error_view.html'):
    t = loader.get_template(template_name)
    return HttpResponseForbidden(t.render({}), content_type='text/html')
