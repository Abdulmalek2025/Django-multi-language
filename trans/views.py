from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView
from django.utils.translation import gettext as _

class HomeView(TemplateView):
    template_name = 'home.html'
    extra_context = {'title': _('Custome Title')}