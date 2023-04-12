from flask import Blueprint
from time import time
import json
from flask import Flask, render_template, jsonify , request , redirect, session,url_for
from tables import *
api = Blueprint('api',__name__)


@api.route('/api')

def usersdash():
 return "<h1>working</h1>"


@api.route('/api/equipment_dict' , methods=['GET','POST'])
def aja():
  b=sess.query(Equipment_Register).all()
  equip_List =[]
  
  for x in b:
    print("x=",x.Equipment_Descr)
    equip_dict={"Equip_desc":x.Equipment_Descr}
    equip_List.append(equip_dict)
  
  print(equip_List)
  print(b[0])
  print(x.id)
  data = json.dumps(equip_List)
  
  return data

@api.route('/api/submit_report' , methods=['GET','POST'])
def submit_report():
    print("ongoing")
    data=request.data
  
    #data = json.loads(data)
    #data["color"] = "red"
    print("this:",data)
    print(type(data))
  
    return "Done"    
