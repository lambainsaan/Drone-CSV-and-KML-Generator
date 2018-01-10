import xml
from fastkml import kml
from shapely.geometry import Point

def execute():
    """ This method binds together different modules to generate kml file
    """

    import helper
    import srt


    ######### Asking for necessary user inputs

    kml_file = helper.get_output_file_name(".kml")

    srt_dir = helper.get_srt_dir() 

    path = srt.path_from_srt_files(srt_dir)


    ########## Generating the KML document

    k = kml.KML()

    doc_tag = kml.Document() # Create Document tag

    k.append(doc_tag) # Add the document tag to the kml

    for lonlat in path:
        # Add every lonlat to the document tag
        placemarker_tag = kml.Placemark()
        placemarker_tag.geometry = Point(lonlat)
        doc_tag.append(placemarker_tag)

    ########### Writing to the KML file
    
    try:
        with open(kml_file, mode='w') as kml_file:
            kml_file.write(k.to_string())
    except FileNotFoundError:
        # If file not found.
        print("File not found please create the file and then rexecute the script.")
        exit()

execute()
