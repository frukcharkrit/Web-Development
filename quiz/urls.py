from django.urls import path
from quiz.views import get_question, post_question

# route
urlpatterns = [
    path('question/', get_question),
    path('question/create', post_question),
]