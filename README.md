# Just-Lane

## READ ME
A detailed guide to use the product.



### Getting Started :

#### *Traffic Congestion Predictor* 
  There are 3 html files :
  home.htm 
  result.htm
  map.htm
	All the three files can be found in the templates folder in the drive link, 
  It’s important that they are kept in a folder called “templates”, post download.

  The “app.py” file which you can find in the drive link, should be executed on the command prompt for the model to work.

  After entering the directory where all the files are, type the following command:
                python app.py 

  If it successfully runs, copy the hostname and paste it in a browser.
  You will see a web page, where the desired inputs can be entered.

  Note: Make sure to put the path of your map.htm file,in the app.py file.

#### *Vehicle Analysis*

  Execute the Vehicle_Analysis.py file which also includes the front end. A new window (feather icon ) opens where the input must be given. On the button click, the output is displayed on the same tkinter window.

### Sample Inputs :

#### *Traffic Congestion Predictor* 

  On the first page of the model, you have three options, one is to predict based on current location and time, or simply take current location and enter required time and the third option is to predict based on latitude, longitude and time taken as input.

  You can use the sample input given as follows :

  Time(hour)	:    11
  Latitude 	:    9.3577880859375
  Longitude	:    76.58914947509766

#### *Vehicle Analysis*

  Vehicle Id to be provided in the following format,
  12DF03C6:19890203641970688685
  
### Prerequisites  :

  pygmaps( version   0.1.1 )
  Geopandas( version  0.6.1 )
  geocoder( version   1.38.1)
  
### References to the files :

####  *Model_loc_time_knn(scikit).ipynb / .py*
  Code for the development of the model constructed using the scikit learn library. Uses ‘ data_loc_time.csv ’ .

####  *model_loc_time_knn.pkl*
  Pickled model. File holds the saved state of the trained model, used in app.py

####  *Vehicle_Analysis.ipynb / .py*
  Python code used to perform the analysis of the vehicles. Includes front end as well. Uses ‘ alert_data_.csv ’ .

####  *app.py* 
  Python code used to deploy the model saved in the file, ‘model_loc_time_knn.pkl’ developed with the Flask framework.

#### *home.htm , result.htm and map.htm*
  HTML and CSS code used for the web pages.
  home.htm is the first page, where the user enters the input.
  result.htm is the page where the results based on the prediction model are displayed.
  map.htm is where the point based on the input is displayed on the map.  


 

