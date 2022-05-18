#Imported modules
import os
import time
import shutil

#Initiation print statements
print('Welcome to the Old File/Folder Remover Program.')
print('This program deletes files and folders based on their creation time.')
print("Please make sure you've backed up any important files or folders.")
print("Any deleted data cannot be recovered via the Recycle Bin.")
print('Also make sure the program file is in the same folder as the folder you wish to clean.')

#User inputs
threshold_min = int(input("Delete data older than (in minutes) : "))

#Universal scope constants
path = os.getcwd()
objList = os.listdir(path)
threshold_sec = threshold_min * 60
epoch_lasped = time.time()

#Additional prints
print('Deleting files and folders created before: ' + time.ctime(epoch_lasped - threshold_sec))

#Main loop - checks and compares creation time of each file/folder for deletion (excluding the main py file)
for i in objList:

    #Excludes the main py file
    if i == 'oldFileRemover.py':
        continue

    #Local scope variables
    objPath = path + '/' + i
    epoch_lasped_compensated = epoch_lasped - threshold_sec
    epoch_fileCreation = os.stat(objPath).st_ctime
    objSeg = []
    objType = ''
    toBeDeleted = ''

    #Object type segregator (File/Folder)
    objSeg = os.path.splitext(objPath);
    if objSeg[1] == '' :
        objType = 'Folder'
    else:
        objType = 'File'

    #File/folder check and deletion
    if epoch_fileCreation < epoch_lasped_compensated :
        if objType == 'File':
            os.remove(objPath)
            toBeDeleted = 'Yes'
        elif objType == 'Folder':
            shutil.rmtree(objPath)
            toBeDeleted = 'Yes'
    else:
        toBeDeleted = 'No'


    #Print statements for user
    print(objType + ' Name: ' + i)
    print('Creation Time: ' + time.ctime(epoch_fileCreation))
    print('Deleted: ' + toBeDeleted)
    print('')

#Ending prints
print("Cleanup Successful.")
print("Exiting...")