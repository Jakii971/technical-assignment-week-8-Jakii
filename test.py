from flask import Flask, request
from db import save_to_db

app = Flask(__name__)

@app.route('/')
def entery_point():
    return 'Jaki horang kayaa amiin...'

@app.route('/data', methods=['GET', 'POST'])
def data2():
    kecepatan = request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    save_to_db(kecepatan=kecepatan, latitude=latitude, longitude=longitude)
    return{
        "message": "Sukses memasukkan data ke dalam database"
    }

if __name__ == '__main__':
    app.run(debug=True)