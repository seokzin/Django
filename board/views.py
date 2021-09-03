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
    question = Question.objects.get(pk=pk)
    context = {
        'question': question,
    }
    return render(request, 'board/edit.html', context)


def update(request, pk):
    question = Question.objects.get(pk=pk)
    question.title = request.POST.get('title')
    question.category = request.POST.get('category')
    question.content = request.POST.get('content')
    question.save()

    return redirect('board:detail', question.pk)

def delete(request, pk):
    question = Question.objects.get(pk=pk)

    if request.method == 'POST':
        question.delete()
        return redirect('board:index')
    else:
        return redirect('board:detail', question.pk)