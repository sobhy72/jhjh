from flask import Blueprint
import credent
from credent import *
from tables import *

#user reports
#check user
#get report no & date
#render report data
#view report data


reports = Blueprint('reports',__name__)

#Get Report No and its date
@reports.route('/dailyreport')
def dailyreport():
  #check session validity /// if not valid --- user to login again
  credent.credent()
  if not 'loggedin' in session:
        return redirect('/')
  userid = session['id']
  data=sess.query(Report_reg).filter(Report_reg.eng_id==userid)
  print("type request: ",type(data[0].report_date))
  return render_template('reportslog.html' , data=data) 

@reports.route('/reportdisp/<repno>')
def reportloadert(repno):
  #check session validity /// if not valid --- user to login again
  credent.credent()
  if not 'loggedin' in session:
        return redirect('/')
  userid = session['id']
  #Get report data
  repno = repno
  data=sess.query(Report).filter(Report.report_no==repno)
  print (data)
  print(type(data))
  return render_template('reportdata.html' , data=data)
  
  

  
  

