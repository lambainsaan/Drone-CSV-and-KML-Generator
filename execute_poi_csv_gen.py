""" This module generates the CSV file for Points of Interest.
"""

import logging

import helper

helper.set_logging(logging)


def execute():
    """ Gets the required user input and generates the output in the specified CSV file
    """
    import generator_csv
    import poi_scanner

    ########## Getting user input

    image_dir = helper.get_input_dir("images")
    csv_dir = helper.get_input_dir("CSVs")
    dist = helper.get_dist()
    output_file = helper.get_output_file_name(".csv")

    ########## Generating the filtered CSV for the Point of Interest (POIs)
    
    poi_scanner.generate_filtered_csv_for_pois(
        csv_dir, dist, image_dir, output_file)

execute()
