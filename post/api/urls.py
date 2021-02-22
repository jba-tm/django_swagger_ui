from django.urls import include, path

from rest_framework_swagger.views import get_swagger_view

from .routers import router


schema_view = get_swagger_view(title='Pastebin API')

app_name = 'post'
urlpatterns = [
    path('', include(router.urls)),
    # path('post/', PostViewSet.as_view({'get': 'list'}), name='post-list')
]
