#Untuk menjalankan requirements yang akan diinstall
pip3 install -r requirements.txt 

# Membuat virtual enviroment
python3 -m venv login-env

# Mengaktifkan virtual environment
source login-env/bin/activate

# Menjalankan project
uvicorn main:app --reload 
