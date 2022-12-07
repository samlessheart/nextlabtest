from django.shortcuts import render, redirect
from .forms import OurAppsForm, TasksForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .decorators import staff_required
from .models import OurApps, Tasks
from django.contrib import messages
from PIL import Image


def resize_image(image):
    print()
    print(img.height)
    img = Image.open(image)
    if img.height > 300 or img.width > 300:
        output_size = (300,300)
        print(img.height)
        return img.thumbnail(output_size)
    return img


#  home page
def home(request):
    return render (request, "pages/home.html")



# Admin Dashboard wherer admin can add apps
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



# User Dashboard where user will see the task to complete
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
        if form.is_valid():
            photo = form.cleaned_data.get('photo')
            
            user = request.user
            task = Tasks.objects.create(photo=photo, user= user, apps=objects)           
            task.save()
        messages.success(request, f"You have completed the Task you got {objects.points} points for it.")
        return redirect( 'userdash')
    
    return render(request, "pages/taskcomplete.html", context)


# profile view where user will see his points and completed tasks
@login_required(login_url='/account/login/')
def profiledash(request):
    objects = OurApps.objects.filter(tasks__user = request.user)

    context = {'objects':objects}
    return render(request, 'pages/profiledash.html', context)
