from flask import Flask, render_template, jsonify , request
from database import engine
from sqlalchemy import text


app = Flask(__name__)
items = 2

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
  }
]

def load_activities_from_db():
  with engine.connect() as connection:
    result = connection.execute(text("select * from activities"))       
    activities = []
    for row in result.all():
      activities.append(dict(row._mapping))
    return activities  
  


@app.route("/")
def hello_jovian():
    return render_template('home.html', 
                           jobs=JOBS, 
                           company_name='Jovian')
  
  
@app.route("/report/<id>" , methods=('GET','POST'))
def report_items(id):
  
  global items
  activities = load_activities_from_db()
  #print('done',values[0]['item'],values)
  
  if request.method == 'POST':
    prn = request.form
    #print(prn)
    
    if request.form.get('check') != None:
      items = int(request.form['hidval']) + 1  
      print(items)
      values = request.form     
      return render_template('report.html' , items = 
     items , value = activities)
     
    else:
     values = request.form.getlist('item')
      
     print(values)
     print(values[1])
     return render_template('report.html' , items = 
   items , value = values)
     
  return render_template('report.html' , items = 
   2 , value = activities )

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)