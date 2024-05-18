import os

from shutil import make_archive
from termcolor import colored

from config import WORKING_DIR

class MyClass:

    def run(self):

        for folder in os.listdir(WORKING_DIR):
            print(colored(f"Processing {folder}", 'green'))

            tempFile = WORKING_DIR + "temp"

            # DO FOLDERS
            #make_archive(tempFile, 'zip', WORKING_DIR + folder)

            # DO FILES
            make_archive(tempFile, 'zip', WORKING_DIR, folder)

            os.rename(tempFile + '.zip', WORKING_DIR + folder + '.cbz')

        #file = open('errors.dat', 'r')
        #Lines = file.readlines()
        #
        #count = 0
        #
        #for line in Lines:
        #    count += 1
        #    strippedLine = line.strip()
#
        #    print(colored(f"Processing {strippedLine}", "green"))
#
        #    fileLocation =  strippedLine.replace('/data/','/media/user/drive/')
        #    file = os.path.basename(strippedLine)
        #    fileTarget = f'{WORKING_DIR}{file}'
#
        #    print(colored(f'Copying from {fileLocation}', "cyan"))
        #    print(colored(f'          to {fileTarget}', "cyan"))
#
        #    copyfile(fileLocation, fileTarget)
#
        #    fileType = file.split('.')[-1]
        #    fileName = file.replace(f'.{fileType}', '')
#
        #    extractedFilesLocation = WORKING_DIR + fileName
        #    tempFile = WORKING_DIR + 'temp'
#
        #    if fileType == "cbr":
        #        rf = rarfile.RarFile(fileTarget)
        #        rf.extractall(path=extractedFilesLocation)
#
        #        send2trash.send2trash(fileTarget)
        #        make_archive(tempFile, 'zip', extractedFilesLocation)
        #        send2trash.send2trash(extractedFilesLocation)
#
        #        os.rename(tempFile + '.zip', WORKING_DIR + fileName + '.cbz')
        #    else:
        #        print(colored(f'File Type {fileType} not supported.'))
        