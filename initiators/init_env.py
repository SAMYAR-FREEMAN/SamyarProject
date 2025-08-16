import os 
from dotenv import load_dotenv

jwt_key= None
db_name= None
db_host= None
db_port= None

def load_env_var():
    global jwt_key, db_name, db_host, db_port
    load_dotenv()
    jwt_key = os.getenv("jwt_key")
    db_name = os.getenv("db_name")
    db_host = os.getenv("db_host")
    db_port = os.getenv("db_port")
