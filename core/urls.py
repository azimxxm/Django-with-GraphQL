from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
    # Books Apps
    path('books/', include('books.urls')),
    # Quiz Apps
    path('quiz/', include('quiz.urls')),
    # GraphQL URL
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
