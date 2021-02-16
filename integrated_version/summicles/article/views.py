from django.shortcuts import render
# from django.views.generic.edit import FormView
from rest_framework.filters import SearchFilter
# from django.db.models import Q
from rest_framework import generics, mixins
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
import os

from .models import Article
from .serializers import ArticleSerializer
# from .forms import SearchForm

# Create your views here.

# class SearchFormView():
#     form_class = SearchForm


class MainAPI(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Article.objects.all()
    filter_backends = [SearchFilter]
    serializer_class = ArticleSerializer

    search_fields = ['category', 'title', 'article_date', 'contents', 'newspaper', 'tag']

    def get_queryset(self):
        return Article.objects.all().order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PoliticsAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(category='정치').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EconomicAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(category='경제').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SocietyAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(category='사회').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CultureAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(category='문화').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ForeignAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(category='국제').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DigitalAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(category='IT/과학').order_by('article_date')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
