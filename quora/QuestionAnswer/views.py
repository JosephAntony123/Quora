from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework import generics
from django.contrib.auth.decorators import login_required


def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions})


def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answer_set.all()
    context = {'question': question, 'answers': answers}
    return render(request, 'question_detail.html', context)


@login_required
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('QuestionAnswer:question_list')
    else:
        form = QuestionForm()

    return render(request, 'create_question.html', {'form': form})


@login_required
def answer_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('QuestionAnswer:question_detail', question_id=question_id)
    else:
        form = AnswerForm()

    answers = question.answer_set.all()
    context = {'form': form, 'question': question, 'answers': answers}
    return render(request, 'answer_question.html', context)


@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.user not in answer.likes.all():
        answer.likes.add(request.user)
    return redirect('QuestionAnswer:question_detail', question_id=answer.question.id)


@login_required
def unlike_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.user not in answer.unlikes.all():
        answer.unlikes.add(request.user)
    return redirect('QuestionAnswer:question_detail', question_id=answer.question.id)


class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerListAPIView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerDetailAPIView(generics.RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
