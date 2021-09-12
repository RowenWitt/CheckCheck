# CheckCheck
Modeling wave-heights at the beach

Currently there is an EC2 instance grabbing the new data for the database periodically, running on a Cron job.  I wasn't sure where to put the code for that EC2 instance, so it's in a directory called `Chronos` ... Not all the code for the Chronos API can be included because it would mean dumping the whole instance, which would be annoying, so if there's issues raise an issue on the Repo.

Most of the update data functions shouldn't be used within this application, all DB updates should be run automatically through `Chronos` and this side of the application should only be pulling down data from the DB & S3 bucket then doing Fourier Imputation then weaving that data together for training or inference.

## TODO

- Migrate all DBs to new model structure

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
Grabbing the GRIB files from NOAA is simple enough, I shouldn't even have to use Selenium.  Storing and retrieving the files may prove more difficult... loading the files into memory could swamp my RAM and then CPU trying to account for it.  If that happens on my computer it will change the calculus for the final deployed backend API (2 APIS probably).  Assuming there's no crash, training the model may require training the same model a number of times iteratively in order to get through the entire dataset.  This may be annoying, and may require date/time shuffling, but should be easy enough. 

The biggest headache from the satellite data will increasing the period of predictions (Fourier something for time series).  The second biggest headache from the satellite data will be relating the tide data to the focal points of the model.

#### VALIDATION
Running the Swrobel's surfline data grabber should be fairly simple.  I may need to install Ruby but that's not a big deal.  I also may need to get a Surfline Account so I can use their API, also no big deal.  An additional API key from MagicSeaweed would also be nice -- I wonder if they'd support being my validation data?  This should be one of the easiest parts of the project, though I may need to wait a month to have the full observations I want.  I considered reaching out to Swrobel to get some data from him directly, but for whatever reason I think he won't be helpful.


#### COMBINATION

I should be able to combine all of this data into a 4 dimensional matrix ... (lat, long, time, data) with the data dimension containing 7-10 sub-dimensions.  That should be fairly simple to convert to a Tensor for PyTorch (dammit).

-- Make it happen tomorrow morning

