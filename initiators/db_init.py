from mongoengine import connect

db = None
def db_init():
    try:
        global db
        db = connect(
            "SamyarProject",
            host = "localhost",
            port = 27017,
        )
    except Exception as e:
        print(f"Error while connecting to database : {e}")
    print("Connection to database established")
    


