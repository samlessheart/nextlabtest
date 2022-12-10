NextLabs Test

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




API ENDPOINTS


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



Problem Set I - Regex
Please refer the file "regex_test.py"

Problem Set 2 - A functioning web app with API
Please follow below link-
https://nextlabtest-production.up.railway.app/




Problem Set 3

A)
In couple of my projects i have used Celery for automating the django tasks even in all ofthem i Have used Redis as a messagebroker. one of the reason for choosing Redis was it is lightweight, it doesn't require lots of time and effort to setup. Certaily as i have read on some articles it seems that Redis is not very reliable and it doesnt scale for large projects. in this instances we have choices like RabbitMQ or Kafka. which supports large scale projects and are reliable.


B)  
Django Vs Flask, 
if the application is not database driven and if it is only consist of some static pages and it contains only small logic behind it, it would be better to use flask than django, as it will be easy to setup and start project with Flask. 
While Django is good at what it does it comes with lot of things preinstalled, due to which it has little complexity to it. 
one of the best thing about django it comes with lot of additional things like User authentication,  sqlite databse(not recommended for production obviously) and its own ORM , which make it very easier to build a large scale website within short amount of time.



Deployment Process 
(This is steps are specific for "Railway.app", steps for different cloud service may vary)
Requirements - 
1) Profile on "github"
2) Profile on "Railway.app"

Process Steps - 
1) Create the "requirements.txt" file by using commnand "pip freeze > requirements.txt"
2)Edit settings.py "ALLOWED_HOSTS" change to -  ALLOWED_HOSTS = ["*"]
3)add "Procfile", filename should be "Procfile" without extension
4)add following line in the Procfile without quotes - "web: gunicorn nextlab.wsgi --log-file -"
5) add "runtime.txt" file 
6)add following line in the Procfile without quotes "Python-3.9.9" (currently as on date "Railway" suports python 3.9 and below version only )
7)create git repository on github, push the code on this repository
8)login into "Railway.app"
9) Click on "New Project" button
10)Select "Deploy From GitHub repo" from the option Presented
11)Select "Configure Github App" from the option Presented
12)a new window will popup which will ask for guithub password.
13)Give access to this Github Repository to "Railway.app"
14)Select the Git repositoy from the options which you want to deploy
15)Click on "Add variable"
16)Add the necessary environment variables e.g. "SECRET_KEY"
17)Deployment process will start once all the variables has been added.
18)Click on the Deployment tab, it will show the status of the deployment.
19) click on the link shown in the deployment tab, the hosted app will open in new tab.
