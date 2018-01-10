"""
This module contains helper functions for processing the files and generating properly formatted files. 
"""


def get_files_from_folder(folder, ext):
    """ Returns the files from a folder with the specified extension
    
    
    Arguments:
        folder {[string]} -- [this is the folder in which the files are to be read]
        ext {[string]} -- [the extension of the files that have to be read from the directory]
    
    Returns:
        [list] -- [Returns the names of all the files that have the specified extension 
                    and are inside of the specified directory]
    """
    import logging
    from os import listdir
    from os.path import isfile, join


    try:
        return [f for f in listdir(folder) if isfile(join(folder, f)) and f.lower().endswith(ext)]
    except FileNotFoundError:
        logging.error("Directory " + folder + " does not exists.")
        import sys
        sys.exit()




def filter_files_within_dist(curr_lon_lat, dist, all_images, images_lon_lat_dict):
    """Filter the files within distance of the current latitude longitude pair.
    
    Arguments:
        curr_lon_lat {[tuple]} -- contains the longitude and latitude pair in degrees in the form (longitude, latitude)
        dist {int or float} -- The distance under which the images must lie within to be filtered in
        all_images {List} -- The array of all the image names
        images_lon_lat_dict {Dict} -- A dictionary containing key as image name and lon-lat pair as value
    
    Returns:
        List -- List containing the lon lat as first two elements and filtered images seperated by | as the third argument
    """
    from geopy.distance import vincenty

    return list(filter(lambda img: vincenty(curr_lon_lat, images_lon_lat_dict[img]).meters < dist, all_images))

def is_lon_lat(lon, lat):
    """ Checks if the lonlat pair is correct
    
    Arguments:
        lon {Float} -- Longitude
        lat {Float} -- Latitude
    
    Returns:
        Boolean -- true if the cordinate lies in the correct domain
    """

    if (0 <= lon and lon <= 180) and (0 <= lat and lat <= 90):
        return True
    return False 


############
#
# Accessor Functions with necesary error checking in the user input.
#
############



def get_dist():
    """ Accessor function to get the dist from the user
    
    Returns:
        float -- Returns the floating point distance that user wants the images within
    """
    import logging
    try:
        return float(input(
            "Enter the distance you want the images to be within in the CSV file (float or int): "))
    except ValueError:
        logging.error("Enter a float or integer value.")
        exit()





def get_output_file_name(ext):
    """Accessor function to get the file name of the csv file the user wants to put the csv generated data in.  
    Arguments:
        ext [String] -- the extension of the file 
    Returns:
        string -- the name of the CSV file user wants to print to.
    """
    import logging
    output_file = input("Enter the " + ext.upper() + " file name to process the output in: ")

    # If the file does not end with .csv extension generate error.
    if not output_file.lower().endswith(ext):
        logging.error("The file must end with " + ext + " extension")
        exit()

    return output_file


def get_input_csv_dir():
    """Accessor function to get the file name of the csv file the user wants to put fetch the csv data from.  
    
    Returns:
        string -- the name of the CSV file user wants to read from
    """
    csv_dir = input("Enter the name of the directory that contains CSV input files : ")

    return validate_dir(csv_dir)



def get_image_dir():
    """Gets the image directory from the user
    
    Returns:
        String -- The name of the directory that user inputs
    """
    image_dir = input("Enter the path to images :")
    
    return validate_dir(image_dir)



def get_srt_dir():
    """Gets the image directory from the user
    
    Returns:
        String -- The name of the directory that user inputs
    """
    srt_dir = input("Enter the path to srt files :")
    
    return validate_dir(srt_dir)



def validate_dir(path):
    """ Validates if the path is a directory, returns path if path is valid.

    Arguments:
        path {String} -- The path that has to be validated, for being a directory.

    Returns:
        String -- The path to the directory if the directory is existant.
    """
    import logging
    import os

    if os.path.isdir(path):
        return path
    else:
        logging.error(path + " is not an existing directory.")
        exit()


def validate_file(file_name):
    """ Validates if the file_name is a file, returns path of file if it file_name is valid file.

    Arguments:
        file_name {String} -- The path that has to be validated, for being a file.

    Returns:
        String -- The path to the file if the file is existant.
    """
    import logging
    import os

    if os.path.exists(file_name):
        return file_name
    else:
        logging.error(file_name + " is not an existing file.")
        exit()
