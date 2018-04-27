from django.shortcuts import render
from django.views import generic
from .models import Groups

# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(
        request,
        'index.html'
    )

def groups(request):
    """The groups we support"""
    groups = Groups.objects.order_by('date_added')
    context = {'groups': groups}
    return render(
        request,
        'groups.html',context
    )