from django.shortcuts import render, redirect
from .forms import OurAppsForm, TasksForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .decorators import staff_required
from .models import OurApps, Tasks
from django.contrib import messages


# home redirect for admin or user 
def home(request):

    return render (request, "pages/home.html")



# Admin Dashboard
@login_required
@staff_required
def admindash(request):
    form = OurAppsForm()
    if request.method == "POST":
        
        form = OurAppsForm(request.POST, request.FILES)
        print(f'\n{form.is_valid()}\n')
        if form.is_valid():        
            form.save()
            
        messages.success(request, f'An App has been added')
        return redirect('home')

    return render(request, "pages/admin_dash.html", {'form':form})




# User Dashboard 
@login_required(login_url='/account/login/')
def userdash(request):
    objects = OurApps.objects.exclude(tasks__user = request.user)

    context = {'objects': objects}

    return render(request, "pages/user_dash.html", context)


# To see the details of the task and to add task
@login_required(login_url='/account/login/')
def taskcomplete(request, pk):
    objects = OurApps.objects.get(id=pk)
    if request.user.tasks.filter(apps = objects).count() > 0:
        messages.warning(request, 'You have already completed this Task')
        return redirect('userdash')

    context = {'objects': objects}
    form = TasksForm()
    context['form'] = form
    if request.method == 'POST':
        form = TasksForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            photo = form.cleaned_data.get('photo')
            user = request.user
            task = Tasks.objects.create(photo=photo, user= user, apps=objects)
            task.save()
        messages.success(request, f"You have completed the Task you have got {objects.points}")
        return redirect( 'userdash')
    

    return render(request, "pages/taskcomplete.html", context)
