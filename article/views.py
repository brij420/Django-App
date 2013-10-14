# Create your views here.
#===============================================================================
# from django.http import HttpResponse
# from django.template.loader import get_template
# from django.template import Context
# from django.views.generic.base import TemplateView
# 
# def hello(request):
#     t=get_template('hello.html')
#     html=t.render(Context({'name':'Brijesh Kumar'}))
#     return HttpResponse(html)
# 
# class HelloTemplate(TemplateView):
#     template_name='hello.html'
#     
#     def get_context_data(self,**kwargs):
#         context=super(HelloTemplate,self).get_context_data(**kwargs)
#         context['name']='Brijesh Kumar'
#         return context
#===============================================================================

from django.shortcuts import render_to_response
from article.models import Article

def articles(request):
    return render_to_response('articles.html',{'articles':Article.objects.all()})

def article(request,article_id=1):
    return render_to_response('article.html',{'article':Article.objects.get(id = article_id)})
    
    