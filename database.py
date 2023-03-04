from sqlalchemy import create_engine
import os  

db_connection_string = os.environ['DB_CONN_DEV']

engine = create_engine(db_connection_string,
  connect_args={
      "ssl": {
          "ssl_ca": "/etc/ssl/cert.pem"
                    }
    } , echo = True)

  
  

  

  
   
