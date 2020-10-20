# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)
app.config["DEBUG"] = True

cred = credentials.Certificate("myprojectapi.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

users = db.collection(u'users')

@app.route('/', methods=['GET'])
def home():
    return "Hello Trần Trọng Nghĩa_16012391"

@app.route('/user', methods=['GET'])
def getNextFromCurrent():
    return jsonify([doc.to_dict() for doc in users.stream()])

@app.route('/user/create/<string:x>/<string:y>/<int:z>/<int:t>', methods=['GET'])
def getCreate(x,y,z,t):
    try:
        users.add({
            'ma':x,
            'ten':y,
            'tuoi':z,
            'luong':t
            })
        return jsonify({'success': True})
    except Exception as e:
        return f"Error : {e}"
    
@app.route('/user/update/<string:x>/<string:y>/<int:z>/<int:t>', methods=['GET'])
def getUpdate(x,y,z,t):
    for doc in users.where('ma','==',x).stream():
        ma = doc.id
    try:
        ma2 = str(ma)
        users.document(ma2).update({
            'ma':x,
            'ten':y,
            'tuoi':z,
            'luong':t
            })
        return jsonify({'success': True})
    except Exception as e:
        return f"Error : {e}"
    
@app.route('/user/delete/<string:x>', methods=['GET'])
def getDelete(x):
    for doc in users.where('ma','==',x).stream():
        ma = doc.id
    try:
        ma2 = str(ma)
        users.document(ma2).delete()
        return jsonify({'success': True})
    except Exception as e:
        return f"Error : {e}"

if __name__ == '__main__':
    app.run()