"""
WEB_BASICS EXAM PREPARATION

Step 1
- extract recourses\templates in templates folder
- create a [staticfiles] folder on the level of templates
- put the statick files [images, css] in the [staticfiles] folder


# CREATING A NEW APP
1. terminal -> python manage.py startapp [new app name]
2. move the new app into the project dir [main is in 'petstagram' folder]
3. add the new app in 'settings' -> INSTALLED_APPS -> INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + NEW_NAME_APPS
4. create 'urls.py' inside the new app
5. include app's urls.py into the project's [petstagram] urls.py
"""

"""
# CREATE A NEW MODEL/CLASS
1. models.py -> class name
2. create Fields(Columns)
3. use built-in validators, 
if you need specific ones you can create custom validators -> create 'validators.py' inside the app 
"""