from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .models import Article, Section, Status

class ArticleListView(ListView):
    template_name="articles/list.html"
    model = Article

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["article_list"]= Article.objects.order_by("created_on").reverse()
        return context

class ArticleDetailView(DetailView):
    template_name= "articles/detail.html"
    model = Article
    