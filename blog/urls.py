from rest_framework import routers

from blog.views import ArticleViewSet

article_route = routers.DefaultRouter()
article_route.register(r'articles', ArticleViewSet)

urlpatterns = article_route.urls
