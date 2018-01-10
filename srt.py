""" 
This module contains functions to read and parse the srt file for cordinates.
"""



def path_from_srt_files(srt_file_path):
    """Reads all the srt files in the path and returns the latitude and longitude of the path of the drone as a list 
    
    Arguments:
        srt_file_path {string} -- The path to be scanned for the srt files
    
    Returns:
        list -- The path of the drone in all different srt files stiched together
    """
    import pysrt
    import logging

    import helper
    
    try:
        srt_files = helper.get_files_from_folder(srt_file_path, '.srt')
    except FileNotFoundError:
        logging.error("Could not find the Directory: " + srt_file_path)

    path = []

    # for every srt file open it and
    # for every subtitle in subtitles
    # append the cordinate to the path
    for srt_file in srt_files:
    
        subts = pysrt.open(srt_file_path + '/' + srt_file if not srt_file_path.endswith('/') else srt_file_path + srt_file)
    
        for subt in subts:
    
            try:
                lon_lat = get_lat_longitude(subt.text)
            except ValueError:
                logging.info(srt_file + " file contains subtitle in incorrect form.")
                continue
    
            if not helper.is_lon_lat(lon_lat[0], lon_lat[1]):
                logging.info(
                    srt_file + " file contains lon lat out of bounds.")
                continue

            path.append(lon_lat)

    return path


def get_lat_longitude(text):
    """Gets the latitude and longitude from a line's text representation 
    
    Arguments:
        text {string} -- The text in the format "lat, long"
    
    Returns:
        Tuple - Containing the float based latitude and longitude, throws ValueError if text does not contain number
    """

    arr = text.split(',')
    return (float(arr[0]), float(arr[1]))
