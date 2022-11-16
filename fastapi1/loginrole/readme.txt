#Untuk menjalankan requirements yang akan diinstall
pip3 install -r requirements.txt 

# Membuat virtual enviroment
python3 -m venv loginrole-env

# Mengaktifkan virtual environment
source loginrole-env/bin/activate

# Menjalankan project
uvicorn main:app --reload 

# Install mysql
pip install pymysql
