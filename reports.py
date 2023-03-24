from flask import Blueprint
import credent
from credent import *

#user reports
#check user
#get report no & date
#render report data
#view report data


reports = Blueprint('reports',__name__)

@reports.route('/dailyreport')

def dailyreport():
  
  credent.name()
  return render_template('report.html',rws=2) 