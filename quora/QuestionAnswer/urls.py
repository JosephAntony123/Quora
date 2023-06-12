from django.urls import path
from . import views

app_name = 'QuestionAnswer'

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('create_question/', views.create_question, name='create_question'),
    path('question/<int:question_id>/answer/', views.answer_question, name='answer_question'),
    path('answer/<int:answer_id>/like/', views.like_answer, name='like_answer'),
    path('answer/<int:answer_id>/unlike/', views.unlike_answer, name='unlike_answer'),
    path('api/questions/', views.QuestionListAPIView.as_view(), name='question_list_api'),
    path('api/questions/<int:pk>/', views.QuestionDetailAPIView.as_view(), name='question_detail_api'),
    path('api/answers/', views.AnswerListAPIView.as_view(), name='answer_list_api'),
    path('api/answers/<int:pk>/', views.AnswerDetailAPIView.as_view(), name='answer_detail_api'),
]
