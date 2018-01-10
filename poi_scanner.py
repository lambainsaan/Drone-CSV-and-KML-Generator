""" This module contains code to scan the csv file and generate the required CSVs. 
"""

import csv

import lat_lon


def generate_filtered_csv_for_pois(input_dir, dist, image_dir, output_file):
    """ 
    
    Arguments:
        file_name {String} -- The name of the csv file to be read.
    """
    import logging
    # The dict with the images name and their latitude and longitude
    images_lon_lat_dict = lat_lon.lat_lon_of_images(image_dir)

    # All the images contained in the specified image directory
    all_images = images_lon_lat_dict.keys()

    ########### Writing filtered image for every Point of Interest (POIs) to the CSV file
    try:
        with open(output_file, 'w', newline='') as csv_output_file:
            read_csv_files_and_add_images_for_every_poi(input_dir, dist, csv_output_file, all_images, images_lon_lat_dict)
    except FileNotFoundError:
        logging.error(output_file + " does not exist.")





def read_csv_files_and_add_images_for_every_poi(input_dir, dist, csv_output_file, all_images, images_lon_lat_dict):
    """Reads the csv file for every poi and adds all the filtered images to the output csv file for every poi.

    Arguments:
        csv_output_file -- Output csv file
        all_images {[type]} -- List of all the images
        images_lon_lat_dict {[type]} -- Dictionary with all the images as key and lat-lon as value
    """
    import logging
    import helper
    

    ########## Generating the heading for the output CSV file
    csv_writer = csv.writer(csv_output_file)
    csv_writer.writerow(
            ['asset_name', 'longitude', 'latitude', 'image_names'])

    ########## Generating the rest of the CSV file with filtered images in image_names column
    for file_name in helper.get_files_from_folder(input_dir, '.csv'):
        
        with open(file_name, newline='') as csv_reading_file:
            
            csv_reader = csv.reader(csv_reading_file, delimiter=',')
            
            # For every line in csv input file 
            # Filter the images within dist
            # and write them to the output file
            for row in csv_reader:
                try:
                    lon_lat = list(map(float, row[1:3]))
                
                    if not helper.is_lon_lat(lon_lat[0],
                                             lon_lat[1]):
                        logging.info('The file ' + file_name + ' contains lon-lat outside of domain of lon-lat.')
                        continue
                except ValueError:
                    continue
                
                filtered_images = helper.filter_files_within_dist(lon_lat, dist, all_images, images_lon_lat_dict)

                write_filtered_images_to_csv(csv_writer, row, filtered_images)
        
    
def write_filtered_images_to_csv(csv_writer, row, filtered_images):
    """ Writes the filtered images to csv file
    
    Arguments:
        csv_writer  -- Writer to write to the output file
        row {Tuple or List} -- a line in the input csv line which we use to generate new csv file
        filtered_images {List} -- All the images within certain distance from latitude longitude mentioned in the row 
    """
    csv_writer.writerow([row[0], row[1], row[2],
                         "|".join(filtered_images)])
