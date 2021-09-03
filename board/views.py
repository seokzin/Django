from django.shortcuts import render, redirect
from .models import Question

def new(request):
    return render(request, 'board/new.html')


def create(request):
    question = Question()
    question.title = request.POST.get('title')
    question.category = request.POST.get('category')
    question.content = request.POST.get('content')
    question.save()

    return redirect('board:detail', question.pk)


def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'board/index.html', context)


def detail(request, pk):
    question = Question.objects.get(pk=pk)
    context = {
        'question': question,
    }
    return render(request, 'board/detail.html', context)


def edit(request, pk):
    return render(request, )


def update(request, pk):
    pass


def delete(request, pk):
    pass