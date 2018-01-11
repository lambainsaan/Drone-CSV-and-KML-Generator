""" This module binds together all the other scripts and does the necessary checks on user inputs.
"""

import logging

import helper

helper.set_logging(logging)

def execute():
    """ Gets the required user input and generates the output in the specified CSV file
    """
    import generator_csv

    ######## Getting the input parameters


    image_dir = helper.get_input_dir("images")
    srt_dir = helper.get_input_dir("SRTs")
    dist = helper.get_dist() # The permissive distance within which the images must be
    
    ######## Generating the filtered CSV file
     
    generator_csv.generate_filtered_csv_at_path(srt_dir, image_dir, dist) # Generates the filtered CSV at the path




execute()
