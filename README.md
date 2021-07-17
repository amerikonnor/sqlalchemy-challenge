### This respository is a project that demonstrates the ability to connect to a sqlite database in python using SQLAlchemy, and then analyze and visualize some data using Pandas and Matplotlib. The data comes from a sqlite database of climate data in Hawaii.

## File Structure
1. app.py
* Creates a flask app to run the climate api.
* api routes:
- api/v1.0/precipitation: return precipitation data for the last 12 months
- api/v1.0/stations: returns all the climate stations in the dataset
- api/v1.0/tobs: returns observed temperature from the most active station
- api/v1.0/<start>/<end>: returns minimum, maximum, and average observed temperature for the time period between <start> and <end>
- api/v1.0/<start>: returns minimum, maximum, and average observed temperature for the time period after <start>
2. app_work.ipynb
 * Jupyter notebook testing connection using sqlalchemy
 * Makes sure different queries work for use in the app
3. climate_analysis.ipynb
  * Connects to the sqlite database using sqlalchemy
  * Queries and plots the last 12 months of precipitation data in the database
  * Calculates summary statistics for the precipitation data
  * Finds the most active station; gets minimum, maximum, average observed temperature at station; plots histrogram of last 12 months of observed temperatures at the station
4. Resources
* hawaii.sqlite: database of climate data
* hawaii_measurements.csv, hawaii_stations.csv: data that is contained in the database
