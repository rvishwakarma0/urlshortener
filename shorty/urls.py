
from django.urls import path

from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView
from shortner.views import root,index

urlpatterns = [
    path('graphql/',csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('<str:url_hash>/', root, name="root"),
    path('',index,name="index")

]
