from django.urls import reverse
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory
from .views import *
from .factories import ArticleFactory, UserFactory


class TestArticleViews(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_list_view(self):
        ArticleFactory(title='my article')
        request = self.factory.get(reverse('api:article-list'))
        response = ArticleViewSet.as_view({'get': 'list'})(request)
        self.assertTrue(response.status_code, 200)

    def test_detail_view(self):
        a = ArticleFactory(title='my article')
        request = self.factory.get(reverse('api:article-detail',args=(a.pk,)))
        response = ArticleViewSet.as_view({'get': 'retrieve'})(request, pk=a.pk)
        self.assertTrue(response.status_code, 200)

