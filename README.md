# CheckCheck

Most of this has changed.  Now using Dask and Xarray to speed up satellite data collection.  The main concern now is how big of an instance would be required to run the satellite data processing component.  Also subsetting data by lat/long.

## TODO

- Find best satellite data source (NOAA has a lot of nulls)
- Set up GRIB -> S3 Pipeline
- Set up Fourier Imputation
- Build Model

## ETL FLOW

- GRIB2 data from NOAA goes to S3 Bucket

- Tide data from NOAA goes to postgreSQL DB (DB A, TABLE tide)

- Prediction data from Surfline API goes to postgreSQL DB (DB A, TABLE val)

- Weather data from NOAA goes to postgreSQL DB (DB A, TABLE weather)

- Buoy data from NOAA goes to postgreSQL DB (DB A, TABLE buoy)

### DATA
Right now I theoretically have pipelines grabbing buoy data and weather data.  While the weather data source could be improved upon, well call it good enough for now.  

#### WEATHER
Tenatively solved

#### BUOY
Tenatively solved

#### TIDE
I also grabbed tidal predictions for all kinds of locations going up to 2100, but the predictions seem to diverge from observations fairly quickly.  Ideally tide data would be grabbed daily for the predicted value for tomorrow and the observed value for yesterday.

How do I solve the tide problem at sea?  Worst case I could go without it but is there a matrix overlay of lat/long tide @ time?  That would be helpful.  Likely I can get that from NOAA, or at least sea height.

#### SATELLITE
Tenatively solved

#### VALIDATION
Tenatively solved

#### FOURIER
Not solved

#### BATHYMETRY
V2 CHANGE


#### COMBINATION
Tenatively solved
