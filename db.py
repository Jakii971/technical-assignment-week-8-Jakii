import pymongo # meng-import library pymongo yang sudah kita install
import datetime

# connect to database
client = pymongo.MongoClient("mongodb+srv://Jaki:vFNhKlDYUbghjnbi@cluster0.lhrhnie.mongodb.net/?retryWrites=true&w=majority")
db = client.SIC # ganti sesuai dengan nama database kalian
my_collections = db.long # ganti sesuai dengan nama collections kalian

# Data yang ingin dimasukkan
def save_to_db(kecepatan,latitude,longitude):
    try:
        data = {
           "kecepatan": kecepatan,
            "latitude": latitude,
            "longitude": longitude,
            "timestamp": datetime.datetime.now()
        }

        # insert data
        results = my_collections.insert_one(data)

        print("Data inserted with result", results) # akan menghasilkan ID dari data yang kita masukkan
        return True, None
    except Exception as e:
        return False, str(e)
        