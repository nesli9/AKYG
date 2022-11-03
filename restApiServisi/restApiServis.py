from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

OGRENCILER = {
    '1': {'ad': 'Neslihan', 'yas': 23, 'bolum': 'Mühendislik'},
    '2': {'ad': 'Tuğçe', 'yas': 20, 'bolum': 'Mühendislik'},
    '3': {'ad': 'Cemile', 'yas': 21, 'bolum': 'Mühendislik'},
    '4': {'ad': 'Oğuzhan', 'yas': 22, 'bolum': 'Mühendislik'},
}

parser = reqparse.RequestParser()

class StudentsList(Resource):
    def get(self):
        return OGRENCILER
    def post(self):
        parser.add_argument("ad")
        parser.add_argument("yas")
        parser.add_argument("bolum")
        args = parser.parse_args()
        
        student_id = int(max(OGRENCILER.keys())) + 1
        student_id = '%i' % student_id
        OGRENCILER[student_id] = {
            "ad": args["ad"],
            "yas": args["yas"],
            "bolum": args["bolum"],
        }
        return OGRENCILER[student_id], 201
    
class Ogrenci(Resource):
    def get(self, student_id):
        if student_id not in OGRENCILER:
            return "Bulunamadı", 404
        else:
            return OGRENCILER[student_id]
    def put(self, student_id):
        parser.add_argument("ad")
        parser.add_argument("yas")
        parser.add_argument("bolum")
        args = parser.parse_args()
        if student_id not in OGRENCILER:
            return "Kayıt bulunamadı", 404
        else:
            ogrenci = OGRENCILER[student_id]
            ogrenci["ad"] = args["ad"] if args["ad"] is not None else ogrenci["ad"]
            ogrenci["yas"] = args["yas"] if args["yas"] is not None else ogrenci["yas"]
            ogrenci["bolum"] = args["bolum"] if args["bolum"] is not None else ogrenci["bolum"]
            return ogrenci, 200

    def delete(self, student_id):
        if student_id not in OGRENCILER:
            return "Bulunamadı", 404
        else:
            del OGRENCILER[student_id]
            return '', 204




api.add_resource(StudentsList, '/ogrenciler/')
api.add_resource(Ogrenci, '/ogrenciler/<student_id>')

if __name__ == "__main__":
    app.run(debug=True)
