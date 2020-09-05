from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import Todoform


def index(request):
    todo_list = Todo.objects.order_by('id')

    form = Todoform()

    context = {
        "todo_list": todo_list,
        'form': form,
    }
    
    return render(request, "todo/index.html", context)

@require_POST
def addTodo(request):
    form =Todoform(request.POST)

    print(request.POST['text'])

    return redirect('index')

