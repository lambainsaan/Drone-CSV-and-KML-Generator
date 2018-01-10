""" This module binds together all the other scripts and does the necessary checks on user inputs.
"""

import logging


# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='logs.log',
                    filemode='w')

# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)

# set a format which is simpler for console use
formatter = logging.Formatter(
    '%(name)-12s: %(levelname)-8s %(message)s')

# tell the handler to use this format
console.setFormatter(formatter)

# add the handler to the root logger
logging.getLogger('').addHandler(console)







def execute():
    """ Gets the required user input and generates the output in the specified CSV file
    """
    import generator_csv
    import helper

    ######## Getting the input parameters

    image_dir = helper.get_image_dir()
    srt_dir = helper.get_srt_dir()
    dist = helper.get_dist() # The permissive distance within which the images must be
    output_file = helper.get_output_file_name(".csv")

    
    ######## Generating the filtered CSV file
     
    try:
        generator_csv.generate_filtered_csv_at_path(srt_dir, image_dir, dist, output_file) # Generates the filtered CSV at the path

    except FileNotFoundError:
        logging.error("CSV file " + output_file +
                     " does not exist please create the file, and then re-execute the script.")
        exit()

    except IsADirectoryError:
        logging.error("File" + output_file + " is a directory")
        exit()



execute()
