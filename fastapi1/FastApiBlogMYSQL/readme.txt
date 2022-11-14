#Untuk menjalankan requirements yang akan diinstall
pip3 install -r requirements.txt 

# Membuat virtual enviroment
python3 -m venv blogmysql-env

# Mengaktifkan virtual environment
source blogmysql-env/bin/activate

# Menjalankan project
uvicorn main:app --reload 

# Install mysql
pip install pymysql
