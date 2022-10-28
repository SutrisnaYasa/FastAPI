#Untuk menjalankan requirements yang akan diinstall
pip3 install -r requirements.txt 

# Membuat virtual enviroment
python3 -m venv eco-env

# Mengaktifkan virtual environment
source eco-env/bin/activate

# Menjalankan project
uvicorn main:app --reload 

# Membuat Secret === e8320b4e8668e4d3cdb513a0363ccce70e2cd7fd
open terminal
ketik :
python3
import secrets
secrets.token_hex(20)
