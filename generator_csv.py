"""
This module contains functions to generate the required CSV files.
"""
import csv
from geopy.distance import vincenty

import lat_lon
import srt


def generate_filtered_csv_at_path(path_srt_files, path_image_files, dist):
    """ Generates the CSV file for all the points in the path. 
    
    Arguments:
        path_srt_files {String} -- The path of the SRT files containing the path of the drone
        path_image_files {String} -- The path of the JPG images containing the images taken by the drone
        dist {Float or Int} -- The distance in which the images muste be contained in. 
        output_file {String} -- The name of CSV file to process the data in. 
    """
    import helper
    import logging
    import pysrt
    

    # Get the path of the drone
    srt_files = helper.get_files_from_folder(path_srt_files, '.srt')

    # The dict with the images name and their latitude and longitude
    images_lon_lat_dict = lat_lon.lat_lon_of_images(path_image_files)

    # All the images contained in the specified image directory
    all_images = images_lon_lat_dict.keys()


    path_srt_files = path_srt_files + '/' if not path_srt_files.endswith('/') else path_srt_files


    for srt_file in srt_files:

        with open(srt_file + "_filtered_images.csv", 'w+', newline='') as csvfile:

            srt_file_path = path_srt_files + srt_file # Need full path to open the file later

            csvfile = csv.writer(csvfile) # Writer object for output file

            csvfile.writerow(['time_in_seconds', 'image_names']) # Creating headings

            # For every subtitle if the subtitle is at some second
            # filter all the images within dist of the subtitle
            # and add it to the output csvfile

            for subt in pysrt.open(srt_file_path):
                try:
                    curr_lon_lat = srt.get_lat_longitude(subt.text)
                except ValueError:
                    logging.info(srt_file_path + " file contains subtitle in incorrect form.")
                    continue

                ########## Printing filtered images to the CSV file
                
                if subt.end.milliseconds == 0:
                    csvfile.writerow([helper.convert_subriptime_to_seconds(subt.end) ,"|".join(helper.filter_files_within_dist(curr_lon_lat, dist, all_images,images_lon_lat_dict))])
