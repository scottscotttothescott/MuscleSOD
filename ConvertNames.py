"""
Code to edit Workout txt file names
"""

import os
import datetime

current_path = os.getcwd()

folder_path = os.path.join(current_path,'Workout Notes')

files = os.listdir(folder_path)

new_names = []

for file in files:
    if file == '.DS_Store':
        pass
    else:

        file_path = os.path.join(folder_path,file)

        # Remove "Notes"
        new_name = file[5:]
        # Remove "Workout "
        if new_name[0] == 'W':
            new_name = new_name[8:]

        # Remove ".txt"
        new_name = new_name[:-4]

        # Note: 
        # Could have used a list of strings_to_remove, 
        # and looped through that list, removing from filename if in.

        # Split to day, month, year
        split_name = new_name.split(':')

        # Deal with typo in name (accidental //)
        if '' in split_name:
            split_name.remove('')

        # Format date
        day,month,year = split_name
        if len(year) == 2:
            year = '20' + year
        date = datetime.date(year = int(year), month = int(month), day = int(day))
        clean_date = datetime.datetime.strftime(date,'%Y-%m-%d')
        new_name = clean_date + '.txt'

        new_path = os.path.join(folder_path,new_name)
        new_names.append(new_name)

        os.rename(file_path, new_path)
