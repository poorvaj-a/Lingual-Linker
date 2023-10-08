from flask import Flask,request
from Translate import Translate as m
from plivoService import sendSMS
app = Flask(__name__)
@app.route("/",methods=["POST"])
def home():
    data = request.get_json()
    print(data)
    translation = m(data)
    print(translation)
    
    print(sendSMS(translation,data.get('to_Number'),data.get('from_Number')))
    return '<h1>Done</h1>'
    


if __name__ == "__main__":
    app.run(debug=True)