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
        f'/api/v1.0/#startdate#/#enddate#</br>'
    
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
    
@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)
    most_active = 'USC00519281'
    results = session.query(Measurement.date,Measurement.tobs).\
        filter(Measurement.date > '2016-08-23').\
            filter(Measurement.station == most_active).all()
    session.close()
    return jsonify(results)

@app.route('/api/v1.0/<start>/<end>')
def date_range(start,end):
    session = Session(engine)
    TMIN = session.query(func.min(Measurement.tobs)).\
        filter(Measurement.date >= start).\
            filter(Measurement.date <= end).scalar()
    TMAX = session.query(func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).\
            filter(Measurement.date <= end).scalar()
    TAVG = session.query(func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).\
            filter(Measurement.date <= end).scalar()
    session.close()
    temp_dict = {'TMIN':TMIN,'TMAX':TMAX,'TAVG':TAVG}
    if TMIN is None:
        return (
                f"Something didn't work.<br/>"
                f'Make sure your dates are formatted as YYYY-MM-DD'
        )
    else:
        return jsonify(temp_dict)

@app.route('/api/v1.0/<start>')
def date_start(start):
    session = Session(engine)
    TMIN = session.query(func.min(Measurement.tobs)).\
        filter(Measurement.date >= start).scalar()
    TMAX = session.query(func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).scalar()
    TAVG = session.query(func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).scalar()
    session.close()
    
    temp_dict = {'TMIN':TMIN,'TMAX':TMAX,'TAVG':TAVG}
    if TMIN is None:
        return (
                f"Something didn't work.<br/>"
                f'Make sure your date is formatted as YYYY-MM-DD'
        )
    else:
        return jsonify(temp_dict)

if __name__ == "__main__":
    app.run(debug=True)