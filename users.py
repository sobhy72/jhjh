from flask import Blueprint
from time import time
import json
from flask import Flask, render_template, jsonify , request , redirect, session,url_for

users = Blueprint('users',__name__)

@users.route('/users')

def usersdash():
 return "<h1>working</h1>"


@users.route('/aj' , methods=['GET','POST'])
def aja():
   print("start")
   if request.is_json:
      if request.method=='GET':
         seconds=time()
         return jsonify({'seconds':seconds})        
      if request.method=='POST':
         card_text=json.loads(request.data).get('text')
         new_text=f'I Got: {card_text}'
         return jsonify({'data':new_text})
   return render_template('ajax.html') 

