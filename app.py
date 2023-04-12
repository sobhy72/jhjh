from tables import *
from credent import *
import json
from reports import reports
from api import api
from users import users
import time
import netifaces as nif
from uuid import getnode as get_mac

#declarations
Base = declarative_base()
Session = sessionmaker(bind = engine)
sess = Session()
today = date.today()
d2 = today.strftime("%B %d, %Y")
rws=10
metadata_obj = MetaData()
meta = MetaData()

#app data
app = Flask(__name__)
app.config['SECRET_KEY'] = 'lsjlzjfjdsf lsdjflsdjf'
app.register_blueprint(users,url_prefix='/')
app.register_blueprint(reports,url_prefix='/')
app.register_blueprint(api,url_prefix='/')

#Login_User
@app.route("/",methods=['GET','POST'])
def login():
  if request.method=='POST':
    username=request.form.get("username")
    password=request.form.get("password")
    stmt = select(Engineers_Reg.c.password).where(Engineers_Reg.c.user_name == username)
    res=sess.execute(stmt)
    res = res.fetchall()
    if res:
      print(res[0][0])
      if password == res[0][0]:
          print("Approved")
          b=sess.query(User).filter(User.user_name==username).first()
          session['loggedin'] = True
          session['date']=utc.localize(datetime.now())
          print(session['date'])
          session['id'] = b.id
          session['username'] = b.user_name
          a=login_register(user_name=b.user_name)
          sess.add(a)
          sess.commit()
          return redirect('/report')
         
      else:
        message= "Please Provide Valid Credentials"
        print("not found",message) 
        return render_template('login.html' ,message=message)
  return render_template('login.html')

#testing fuction
@app.route("/test",methods=['GET','POST'])
def tes():  
  session['loggedin']= True
  if session['loggedin']:
    return f"<h1>This is {session['username']}</h1>"
  return f"<h1>Bad Try</h1>"
 
#Report Form
@app.route("/report" , methods=('GET','POST'))
def reportses():
      #Check session validity to keep user signed 
      credent()  
      if not 'loggedin' in session:
        return redirect('/')

      #Get user responsibilites from data base to generate report form
      username=session['username']
      res=select(respons.c.respons).where(Engineers_Reg.c.user_name ==username)           
      res=sess.execute(res)
      res = res.fetchall()
      print(res)
      return render_template('report.html' , res=res  
           ,date=d2,rws=rws)
   
@app.route("/render", methods=['GET','POST'])
def renderdata():
  
  #get user id
  user=session['id']
  
  #save and return report no. and user_id in db reports_reg table
  rep=Report_reg(eng_id=user)
  sess.add(rep)
  sess.commit()
  
  #get report No.
  repno=sess.query(Report_reg).filter(Report_reg.eng_id==user).order_by(desc(Report_reg.report_no)).first()
  print(repno.report_no)
  
  #Get user Report data 
  a = request.form.getlist('area')
  b = request.form.getlist('descr')
  c = request.form.getlist('unit')
  d = request.form.getlist('QTY')
  e = request.form.getlist('maindesc')
  f = request.form.getlist('remarks')
   
  #save user's report data in db
  i=0
  j=len(a)-1
  while i < len(a):
    if i==j:
      n=Report(descr=b[i],main_descr=e[i],area=a[i],qty=d[i], unit=c[i], remarks=f[0], report_no=repno.report_no, eng_id=user)
      sess.add(n)
      sess.commit()
      #time.sleep(1)
    else:
      n=Report(descr=b[i],main_descr=e[i],area=a[i],qty=d[i],unit=c[i],report_no=repno.report_no,eng_id=user)
      sess.add(n)
      sess.commit()
      #time.sleep(1)
    i +=1
  return render_template('report.html',rws = 10)    
  
def mac_for_ip(ip):
    'Returns a list of MACs for interfaces that have given IP, returns None if not found'
    for i in nif.interfaces():
        addrs = nif.ifaddresses(i)
        try:
            if_mac = addrs[nif.AF_LINK][0]['addr']
            print(if_mac)
            print(type(if_mac))
            if_ip = addrs[nif.AF_INET][0]['addr']
            print(if_ip)
            print(type(if_ip))
        except (IndexError, KeyError): #ignore ifaces that dont have MAC or IP
            if_mac = if_ip = None
        if if_ip == ip:
            return if_mac
    return None  
def mac_for_ip2(): 
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    print("mac2:",request.environ['REMOTE_ADDR'])
  else:
    print("mac2:",request.environ['HTTP_X_FORWARDED_FOR']) # if behind a proxy  
  
  mac = get_mac()
  print("mac:",mac)
@app.route("/api/get",methods=['GET','POST'])
 
def get_my_ip():
    mac_for_ip2()
    #data =request.form.get("value")
    data=request.data
    data = json.loads(data)
    data["color"] = "red"
    print("this:",data)
    print(type(data))
  
    return data    
 
  
  #data = request.args.to_dict(flat=False)
  #return jsonify(data)




if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)