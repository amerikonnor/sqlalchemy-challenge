import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
#############################
#Database Setup
#############################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine,reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station
##########################
#Flask Setup
##########################
app = Flask(__name__)

@app.route("/")
def index():
    return(
        f'Welcome to my Climate API<br/>'
        f'Available routes:<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/#startdate#<br/>'
        f'/api/v1.0/#startdate#/#enddate#'
    )

@app.route('/api/v1.0/precipitation')
def prcp():
    session = Session(engine)
    results = session.query(Measurement.date,Measurement.prcp).all()
    session.close()
    prcp_dict = dict(results)
    return jsonify(prcp_dict)

@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    results = session.query(Station.name).all()
    session.close()
    return jsonify(results)
    
if __name__ == "__main__":
    app.run(debug=True)