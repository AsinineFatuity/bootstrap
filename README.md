# Hybrid Django-React Bootstrap
Scripts to bootstrap my hybrid django-react projects set up inspired by 
* The hybrid Python/Django/React Architecture as described by Cory Zue in [this article](https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/integrating-javascript-pipeline/)
* Session based Auth for SPA/Django as described by Nik Tomazic in [this article](https://testdriven.io/blog/django-spa-auth/)
## Run The Script
1. Install Django using your preferred package manager
2. Start a new project by running `django-admin startproject project_name .` The `.` is necessary so that the script references your project easily
3. Ensure you have installed node and npm
4. Run the script `python3 set_up_frontend.py`
5. This will configure webpack, redux and the react app and install all dependecies
6. Add this to your 
   ```python
   #TEMPLATES["DIRS"] list in project/settings.py
   os.path.join(BASE_DIR, "templates")
   #static files section
   STATIC_ROOT = os.path.join(BASE_DIR.parent, "static")
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
   ```
7. Run `npm start` and `./manage.py runserver` in separate terminal windows
8. Navigate to `http://127.0.0.1:8000` and you will see the react home page loaded
9.  Build on from there