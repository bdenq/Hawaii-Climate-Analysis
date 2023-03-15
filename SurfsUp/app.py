# Dependencies
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask,jsonify


engine = create_engine(f"sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect = True)
measurement = Base.classes.measurement
station = Base.classes.station
session = Session(engine)

app = Flask(__name__)

@app.route("/")
def Welcome():
    return (f"""
<h1>Welcome to my Hawaii Climate Analysis!</h1><br/>
Available Routes:<br/>
/api/v1.0/precipitation<br/>
/api/v1.0/stations<br/>
/api/v1.0/tobs<br/>
/api/v1.0/temp/start<br/>
/api/v1.0/temp/start/end<br/>
<p>'start' and 'end' date should be in the format MMDDYYYY.</p>

    """)
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(station.station).all()
    session.close()
    stations = list(np.ravel(results))
    return jsonify(stations)

if __name__ == "__main__":
    app.run() 


