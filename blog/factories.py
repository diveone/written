import factory

from django.contrib.auth.models import User

from .models import Article


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    author = factory.SubFactory(UserFactory)
