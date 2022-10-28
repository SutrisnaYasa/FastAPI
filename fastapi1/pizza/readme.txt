#Untuk menjalankan requirements yang akan diinstall
pip3 install -r requirements.txt 

# Membuat virtual enviroment
python3 -m venv pizza-env

# Mengaktifkan virtual environment
source pizza-env/bin/activate

# Menjalankan project
uvicorn main:app --reload 

# Install mysql
pip install pymysql

#install sqlalchemy & sqlalchemy_utils
pip install sqlalchemy
pip install sqlalchemy_utils

# Create table 
python init_db.py


# install hash password 
pip install werkzeug
