python -m venv venv
. venv/Scripts/activate
pip install -r requirements.txt
touch apps/menu/migrations/__init__.py
touch apps/coworking/migrations/__init__.py
touch apps/booking/migrations/__init__.py
python manage.py migrate
touch apps/users/tests/__init__.py
python manage.py test apps.users -v2