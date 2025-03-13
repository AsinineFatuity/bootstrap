# hybrid-django-react-bootstrap
Scripts to bootstrap my hybrid django-react project set up inspired by 
* The hybrid Python/Django/React Architecture as described by Cory Zue in [this article](https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/integrating-javascript-pipeline/)
* Session based Auth for SPA/Django as described by Nik Tomazic in [this article](https://testdriven.io/blog/django-spa-auth/)
# Run The Script
1. Install and set up django project as usual 
2. Ensure you have installed node and npm
3. Run the script `python3 set_up_frontend.py`
4. This will configure webpack, redux and the react app and install all dependecies
5. Run `npm start` and `./manage.py runserver` in separate terminal windows
6. Navigate to `http://127.0.0.1:8000` and you will see the react home page loaded
7. Build on from there