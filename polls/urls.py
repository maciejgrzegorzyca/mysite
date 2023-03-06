from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /added the qord "surveys" instead of polls
    # ex.survey/5/ instead of polls/5
    # the 'name' value as called by the {% url %} template tag
    path('survey/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/

]

