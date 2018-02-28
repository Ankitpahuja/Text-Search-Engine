import os

# New directory for every website that you crawl

def create_dir_per_website(directory):
    if not os.path.exists(directory):
        print('Creating Folder for '+directory)
        os.makedirs(directory)

create_dir_per_website('NIITUniversity')
