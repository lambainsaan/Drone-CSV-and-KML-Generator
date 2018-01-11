# SKYLARK Assignment

Output of the code for provided files is in the `solution files` folder.

To execute the code, clone the repo and cd into `Drone-CSV-and-KML-Generator/code`

To execute the scripts you must have  
    
* Python 3.x - instructions on installing python 3.x https://www.python.org/downloads/

* pip 9.0.1- if you don't have pip installed go through the instructions here https://pip.pypa.io/en/stable/installing/, if you have an older version you may upgrade using the command:
```
python -m pip install --upgrade pip
``` 


After setting up the pre-req tools. Execute the following command, if access issue prefix it with sudo:

```
pip install -r requirements.txt
```

There are three scripts of interest.

1. execute_srt_csv_gen.py  - This script scans the srt files (multiple files within the directory specified) and generates csv file with the images withing certain distance. All the parameters are entered as input at the run time. Execute this script using :
```
python execute_srt_csv_gen.py
```

2. execute_poi_csv_gen.py - This script scans .csv files in a directory (multiple files within the directory specified) for Points of Interest (POIs) and generates csv with images withing certain distance of POIs. All the parameters are entered as input at the run time. Execute the script using:
```
python execute_poi_csv_gen.py
```

3. kml_generator.py - This script scans SRT file (single file) for the path and generates KML for the path. All the parameters are entered as input at the run time. Execute the script using:
```
python kml_generator.py
```