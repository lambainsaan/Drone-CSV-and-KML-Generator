"""
This module contains functions to generate the required CSV files.
"""
import csv
from geopy.distance import vincenty

import lat_lon
import srt


def generate_filtered_csv_at_path(path_srt_files, path_image_files, dist, output_file):
    """ Generates the CSV file for all the points in the path. 
    
    Arguments:
        path_srt_files {String} -- The path of the SRT files containing the path of the drone
        path_image_files {String} -- The path of the JPG images containing the images taken by the drone
        dist {Float or Int} -- The distance in which the images muste be contained in. 
        output_file {String} -- The name of CSV file to process the data in. 
    """
    import helper

    ########## Getting all the images from the image path

    # Get the path of the drone
    drone_path = srt.path_from_srt_files(path_srt_files)
    # The dict with the images name and their latitude and longitude
    images_lon_lat_dict = lat_lon.lat_lon_of_images(path_image_files)

    # All the images contained in the specified image directory
    all_images = images_lon_lat_dict.keys()


    ########## Printing filtered images to the CSV file

    with open(output_file, 'w', newline='') as csvfile:
        
        # Setting the output file 
        csvfile = csv.writer(csvfile)
        csvfile.writerow(['longitude', 'latitude', 'image_names'])
        
        
        for curr_lon_lat in drone_path:
            # For every longitude-latitude pair in the path
            # Filter all the images that are within dist meters radius 
            # longitude-latitude pair and write it to the csv file
            csvfile.writerow([curr_lon_lat[0], curr_lon_lat[1],
                              "|".join(helper.filter_files_within_dist(curr_lon_lat, dist, all_images,images_lon_lat_dict))])
