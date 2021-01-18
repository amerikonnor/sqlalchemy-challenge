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
        f'Welcome to my Climate API'
        f'Available routes:'
        f'/api/v1.0/precipitation'
        f'/api/v1.0/stations'
        f'/api/v1.0/tobs'
        f'/api/v1.0/<start>'
        f'/api/v1.0/<start>/<end>'
    )

@app.route('/api/v1.0/precipitation')
def prcp():
    session = Session(engine)
    results = session.query(Measurement.date,Measurement.prcp).all()
    session.close()
    prcp_dict = dict(results)
    return jsonify(prcp_dict)
    
if __name__ == "__main__":
    app.run(debug=True)