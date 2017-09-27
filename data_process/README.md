# Data Process scrips for Machine Learning tools for Haze prediction   
###### Zhe Chen £¨³Â†´£©

Generally, there are 3 types of data of observation of atmosphere data in server (Haze01@162.105.94.208, please contact chen (chenzhesms@pku.edu.cn) for key if needed and authorized) 

1. txt
2. excel
3. mat


For now, they are saved in 'PredictHaze' 'AirObsData' and 'WeatherData', and excel format data is saved locally in chen's computer. 

### Usage

1. For txt format data

Call trans.py to convert txt to excel, remember that some configurations might be slightly modified like inputpath and outputpath. 

Call bj.py to generate data especially for one particular location from trans-ed data. 


2. For mat format data

They are saved properly in server and thus it's basically not needed to be modified. If some notea for defination of different variables are needed, please feel free to contact chen.

