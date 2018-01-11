""" This module contains functions to generate KML file for the path of the drone.
"""

import simplekml

import logging

from shapely.geometry import Point
import helper

helper.set_logging(logging)

def execute():
    """ This method binds together different modules to generate kml file
    """
    
    import srt


    ######### Asking for necessary user inputs

    kml_file = helper.get_output_file_name(".kml")

    srt_file = helper.get_input_file_name(".srt") 

    path = srt.path_from_srt_file(srt_file)


    ########## Generating the KML document

    kml = simplekml.Kml()
    
    kml.newlinestring(name="dronepath", description="%s path" %srt_file,
                            coords=path)
    ########### Writing to the KML file
    
    try:
        with open(kml_file, mode='w') as k:
            k.write(kml.kml())
            logging.info("The kml file is written at ./%s"%kml_file )
    except FileNotFoundError:
        # If file not found.
        print("File " + kml_file + " not found please create the file and then rexecute the script.")
        exit()

execute()
