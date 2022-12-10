# NextLabs Test

About the App
user can share screenshot of an installed app and get points for that activity.
admin users can add the app for which users can do the activity


for Admin Users 

on navigating to "Add App" admin users will be shown an form where they can add app data like app image app name app points etc.

For Normal Users

on navigating on Tasks they will be shown a list of the all the tasks and respective points they can earn for that will shown 
on  clicking the complete task they will presented a form whre they can add screenshot of the installed app.
once submitting the form they will gain the respective points.
on clicking the name of the user user will be shown how much points they have earned so far. 
they will be also shown the task they have completed so far.

-----------------------------

**API ENDPOINTS**

1)   /api/applist/
Method Allowed - GET, POST
authentication Required
GET request will return the list of apps that can be done.
for admin users it will return all the apps that has created
only admin users can do POST request through which he can create apps

2) /api/tasklist/
Method Allowed - GET, POST
authentication Required
GET request will return the list of tasks that has been completed by a user
POST requsets, users can add the tasks by which they will gain points apecified for that app

3) /api/profile/
Method Allowed - GET
authentication Required
GET request will return Profile detail like name and points earned by the user

-----------------------------


**Problem Set I - Regex**
Please refer the file "regex_test.py"

**Problem Set 2 - A functioning web app with API**
Please follow below link-
https://nextlabtest-production.up.railway.app/

-----------------------------

**Problem Set 3**

A)
In couple of my projects i have used Celery for automating the django tasks even in all ofthem i Have used Redis as a messagebroker. one of the reason for choosing Redis was it is lightweight, it doesn't require lots of time and effort to setup. Certaily as i have read on some articles it seems that Redis is not very reliable and it doesnt scale for large projects. in this instances we have choices like RabbitMQ or Kafka. which supports large scale projects and are reliable.


B)  
Django Vs Flask, 
if the application is not database driven and if it is only consist of some static pages and it contains only small logic behind it, it would be better to use flask than django, as it will be easy to setup and start project with Flask. 
While Django is good at what it does it comes with lot of things preinstalled, due to which it has little complexity to it. 
one of the best thing about django it comes with lot of additional things like User authentication,  sqlite databse(not recommended for production obviously) and its own ORM , which make it very easier to build a large scale website within short amount of time.

-----------------------------



**Deployment Process**
(These steps are specific for "Railway.app", steps for different cloud service may vary)
Requirements - 
1) account on "github"
2) account on "Railway.app"
3)account on "Cloudinary" (optional, "WhiteNoise" package can be used instead of this)


Steps - 
1)	Create a git repository on GitHub, push the code on this repository
2)	login into "Railway.app"
3)	 Click on "New Project" button
4)	Select "Deploy from GitHub repo" from the option Presented
5)	Select "Configure GitHub App" from the option Presented
6)	a new window will popup which will ask for GitHub password.
7)	Give access to this Github Repository to "Railway.app"
8)	Select the Git repository from the options which you want to deploy
9)	Click on "Add variable"
10)	Add the necessary environment variables e.g., "SECRET_KEY"
11)	Deployment process will start once all the variables has been added.
12)	Click on the Deployment tab, it will show the status of the deployment.
13)	 click on the link shown in the deployment tab, the hosted app will open in new tab.


Additional Steps for using Cloudinary (for serving static and media files)
1)	Create an account on Cloudinary (it's free for limited use, enough for this project)
2)	Copy the following Product Environment Credentials – “Cloud Name” , “API KEY”, “API SECRET”
3)	Create these Environment Variables in “Railway.app”
4)	Add following package in requiremts.txt -  “django-cloudinary-storage”
5)	Modify Setting.py “INSTALLED_APPS” varialble – add 'cloudinary_storage', and 'cloudinary', in it.
6)	add Cloudinary credentials to settings.py - CLOUDINARY_STORAGE = {  'CLOUD_NAME': 'your_cloud_name',    'API_KEY': 'your_api_key',    'API_SECRET': 'your_api_secret' }
7) for more info on cloudinary - "https://pypi.org/project/django-cloudinary-storage/"



