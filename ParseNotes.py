"""
Script to remove html code from notes and create cleaned files.
"""

from bs4 import BeautifulSoup
import os

# Create Paths to html notes, and destination for the cleaned notes
folder = os.path.join(os.getcwd(),'Workout Notes')
destination = os.path.join(os.getcwd(),'Cleaned Notes')

# List all html files.
files = os.listdir(folder)

# Loop through each html file, extract the data, clean, and write to a new file
for file in files:
    filepath = os.path.join(folder,file)

    source = open(filepath, 'rb')
    soup = BeautifulSoup(source,'html.parser')

    # Extract and clean data
    data = soup.find_all('div')
    cleandata = [i.getText() for i in data]

    newnote = os.path.join(destination,file)

    # Write to new file.
    with open(newnote, 'w') as writeTo:
        for i in cleandata:
            writeTo.write(i)
            writeTo.write('\n')

    source.close()


# Check if any files were missed
newfiles = os.listdir(destination)
missingfiles = []
for file in files:
    if file not in newfiles:
        missingfiles.append(file)

print(f'Number of original files is: {len(files)}')
print(f'Number of new files is: {len(newfiles)}')
print(f'Number of broken files is: {len(missingfiles)}')