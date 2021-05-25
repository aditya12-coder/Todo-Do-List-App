from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from main.models import todo
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def todos(request):
	if request.method == "POST":
		title = request.POST.get('title')
		description = request.POST.get('description')
		todo_list = todo(user=request.user, title=title, description= description)
		todo_list.save()
		messages.success(request, 'Successfully Created')

	todo_list = todo.objects.filter(user=request.user).order_by('-date')

	params = {
		'todos':todo_list,

	}

	return render(request, 'main/todo.html', params)




@login_required
def delete_todo(request, id):
    try:
	    todos = todo.objects.get(id=id)
	    user_id = todos.user_id
	    if user_id == request.user.id:
	        todos.delete()
	        messages.success(request, "Assignment was successfully deleted")
	        return redirect('todo')
	    else:
	        messages.error(request, "You are not authorized to carry out this operation")
	        return redirect('todo')

    except Exception as e:
    	messages.error(request, "Someting Error Happened")
    	return redirect("todo")





@login_required
def edit_todo(request, id):
    todos = todo.objects.get(id=id)
    user_id = todos.user_id
    if request.method == "POST":
        current_user = request.user.id
        if current_user == user_id:
            todos.title = request.POST.get('title_edited')
            todos.description = request.POST.get('description_edited')
            is_completed = request.POST.get('is_completed')
            todos.is_completed = request.POST.get('is_completed')
            todos.save()
            messages.success(request, 'Todo was successfully edited.')
            new_data = todo.objects.last()
            return redirect('todo')

        else:
            messages.error(request, "You are not authorized to carry out this operation")
            return redirect('todo')
