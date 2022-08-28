from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from trans.models import MyModel
class HomeView(TemplateView):
    obj = MyModel.objects.get(id=1)
    template_name = 'home.html'
    extra_context = {'title': _('Custome Title'),'obj':obj}