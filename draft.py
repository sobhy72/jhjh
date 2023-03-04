from flask import Flask, render_template, jsonify , request
from database import engine
import sqlalchemy
from sqlalchemy import text , insert , join , select , create_engine, Table, Column, Integer, String, ForeignKey,MetaData
from sqlalchemy.orm import Session

metadata_obj = MetaData()


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
    result = connection.execute(text("select * from reprots"))       
    activities = []
    for row in result.all():
      activities.append(dict(row._mapping))
      print(activities)
      
    return activities  

def pract_sql_r():
  with engine.connect() as connection:
    result = connection.execute(text("select * from reprots"))       
    activities = []
    for row in result.all():
      activities.append(dict(row._mapping))
      print(activities)
    return activities
    
def pr():
  with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO reprots (descr, unit) VALUES (:x, :y)"),
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
    )
    

def test_r():
   m=["A","B","C"]
   with engine.connect() as conn:
     
    conn.execute(
        text("INSERT INTO reprots (descr, unit) VALUES (:x, :y)"),
        [{"x": m[0], "y": m[1]}, {"x": m[2], "y": 10}],
    )
    conn.commit()

def test_a():
      stmt = text("SELECT descr, id FROM reprots WHERE descr > :y ORDER BY descr, id")
      with Session(engine) as session:
         result = session.execute(stmt, {"y": 6})
         for row in result:
          print(f"x: {row.descr}  y: {row.id}")
   
def join_st():
  
    meta = MetaData()
  
    Engineers_Reg = Table(
       'Engineers_Reg', meta, 
       Column('id'), 
       Column('name'), 
       Column('disipline'),
    )
    
    reprots = Table(
       'reprots', meta, 
       Column('id'), 
       Column('eng_id')
       
    )
    j = Engineers_Reg.join(reprots, Engineers_Reg.c.id == reprots.c.eng_id)
    stmt = select([Engineers_Reg]).select_from(j)
    with engine.connect() as conn:  
      result = conn.execute(stmt)
      result.fetchall()
     #The following is the output of the above code −
    #
    ##[
      # (1, 'Ravi', 'Kapoor'),
       #(1, 'Ravi', 'Kapoor'),
       #(3, 'Komal', 'Bhandari'),
       #(5, 'Priya', 'Rajhans'),
       #(2, 'Rajiv', 'Khanna')
    #]


def lrn_md():
  import sqlalchemy
  user_table = Table(
     "user_account",
     metadata_obj,
     Column("id", Integer, primary_key=True),
     Column("name", String(30)),
     Column("fullname", String),
 )
      
@app.route("/")
def hello_jovian():
    return render_template('home.html', 
                           jobs=JOBS, 
                           company_name='Jovian')
  
  
@app.route("/report/<id>" , methods=('GET','POST'))
def report_items(id):
  
  global items
 # activities = load_activities_from_db()
  #print('done',values[0]['item'],values)
  
  if request.method == 'POST':
    #prn = request.form.getlist
    f=request.form.getlist('item')
    print('check')
    #print(prn)
    #k=prn.getlist('item')
    #k=prn['item']
    print('stop')
    print(f,f[0])
    
    #print(k[1])
    #print(prn['2'])
    
    if request.form.get('check') != None:
      items = int(request.form['hidval']) + 1  
      print(items)
      values = request.form     
      return render_template('report.html' , items = 
     items , value = values)
     
    #else:
     #values = request.form.getlist('item')
      
     #print(values)
     #print(values[1])
     #return render_template('report.html' , items = 
   #items , value = values)
     
  return render_template('report.html' , items = 
   2 , value = JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)