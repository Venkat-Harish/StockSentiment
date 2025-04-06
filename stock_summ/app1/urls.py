from django.urls import path
from .views import test, render_query_page

urlpatterns = [
    path('print/',test,name='test'),
    path('query/', render_query_page, name='query_input'),
]
