""" This module contains the code that processes the latitude and longitude related data 
    and file processing to get the latitude and longitude data.
"""




def lat_lon_of_images(path):
    """ Gets the latitude and longitude of all the images in the path and returns it in a dictionary
    
    Arguments:
        path {string} -- The Directory inside of which the files have to be retrieved from.
    
    Returns:
        dict -- A dictionary containing all the files as key and their
                latitude and longitude pair as value.
    """

    import helper
    import logging
    

    file_names = helper.get_files_from_folder(path, '.jpg')
    
    # The latitude and longitude of all the files will be stored in this dict
    lat_lon_file = dict()

    # for every file add the file name as the key
    # and calculate the LAT and LONG for the file
    # and push it as the value for the key (file)
    for file_name in file_names:
        try:    
            lat_lon_file[file_name] = get_degrees_lat_lon(get_exif_lat_lon_data(path + '/' + file_name if not path.endswith('/') else path + file_name))
        except KeyError:
            # If the GPS information is not present in the exif data
            logging.info("The data for file " + file_name + " is missing the GPS data.")
    
    return lat_lon_file






def get_exif_lat_lon_data(file_name):
    """ Gets the exif latitude longitude data from the file in the argument
    
    Arguments:
        f {string} -- path of the file whose exif data is to be read
    
    Returns:
        tuple 2 * 1 -- Returns a tuple containing exif GPSLongitude data as first cordinate and 
                        GPSLatitude as the second cordinate.
    """
    
    import piexif

    piexif_for_file = piexif.load(file_name)

    return (piexif_for_file['GPS'][piexif.GPSIFD.GPSLongitude],
            piexif_for_file['GPS'][piexif.GPSIFD.GPSLatitude])









def get_degrees_lat_lon(lon_lat):
    """ Gets the latitude and longitude as piexif produces, which is in the degree-minute-second format
        it converts the latitude and longitude into the desired format and returns it as a tuple
    
    Arguments:
        lon_lat {tuple 1 * 2} -- the latitude and longitude in the degree-minute-second format
                                the first element is the longitude and second is latitude
    Returns:
        tuple 1 * 2 -- Returns a tuple with first element as longitude and second as latitude in degrees
    """

    lon = convert_to_degress(lon_lat[0])
    lat = convert_to_degress(lon_lat[1])

    return (lon, lat)








def convert_to_degress(value):
    """Helper function to convert the GPS coordinates 
    stored in the EXIF to degress in float format

    Taken from : https://gist.github.com/erans/983821
    
    Arguments:
        value {[tupe 3 * 2]} -- [This is the degree minute second representation of the latitude
                                 or longitude]
    
    Returns:
        [float] -- [the degree represenation of the degree minute second based reperesentation of 
                    latitude or longitude]
    """

    degree0 = value[0][0]
    degree1 = value[0][1]
    degree = float(degree0) / float(degree1)

    minute0 = value[1][0]
    minute1 = value[1][1]
    minute = float(minute0) / float(minute1)

    second0 = value[2][0]
    second1 = value[2][1]
    second = float(second0) / float(second1)

    return degree + (minute / 60.0) + (second / 3600.0)
