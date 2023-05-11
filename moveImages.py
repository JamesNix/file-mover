import csv
import os
from pathlib import Path

checklist = 'specs-tab.csv'               # csv list of filenames to look for
folderToSearch = Path(r'./Uploads2018')             # folder within which to look for files
foundFolder = './MeetingSpecs2018/'              # folder to move found files into

def searchFileName(name):
    with open(checklist) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if name == row[0]:
                print(name)             #+ ' | ' + row[0])
                os.replace('./' + str(folderToSearch) + '/' + name, foundFolder + name)
                return
        csv_file.close()

for entry in folderToSearch.iterdir():
    searchFileName(entry.name)
