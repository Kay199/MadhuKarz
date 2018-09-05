###Setting up Car Rental APP

#1. Git clone the project 

git clone https://github.com/Kay199/MadhuKarz.git

#2. cd MadhuKarz 

#3. Create a virtual environment. 

virtualenv --pyhton=python3 venv


#4. Activate the virtual environment. source venv/bin/activate


#5. Install django 

pip3 install django

#6. Install postgres - python wrapper

pip3 install psycopg2-binary


#7. Run postgres server postgres -D /usr/local/var/postgres/ &

#8. Create a databse 

#9. createdb rentalappdb

#10. cd MadhuKarz

Migrate the database

python3 manage.py migrate

#11. Run the app 

python3 manage.py runserver

#12. localhost:8000/admin

The admin name: Admin
Password: admin123123

#13. Add Cars

#14. localhost:8000/customer/signup

