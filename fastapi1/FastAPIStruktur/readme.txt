virtualenv venv
source venv/bin/activate
pip install fastapi sqlalchemy pymysql uvicorn 
uvicorn index:app --reload
pip install pymysql
