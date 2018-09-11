import sys
from pydriller import RepositoryMining
import csv
from functions import remove_duplicate_commits, dictionary_of_spoon_output
import subprocess

countOfArgs = len(sys.argv)
pathToRepo = None
if countOfArgs == 2:
    pathToRepo = sys.argv[1]
else:
    pathToRepo = '../repository/'
with open('output/pathToRepo.csv', 'w') as myFile:
    myFile.write(pathToRepo)
changes = []
for commit in RepositoryMining(pathToRepo, only_modifications_with_file_types=['.java']).traverse_commits():
        for modification in commit.modifications:
            if modification.change_type is not None:
                extOfFile = modification.filename[modification.filename.find('.') + 1:]
                if extOfFile == 'java' and (modification.change_type.name == 'MODIFY') or \
                        (modification.change_type.name == 'RENAME'):
                    changes.append([commit.parents[0], modification.old_path, commit.hash, modification.new_path])
with open('output/changes.csv', 'w') as myFile:
    wr = csv.writer(myFile)
    wr.writerows(changes)
listOfCommitsToIterate = remove_duplicate_commits(changes)
with open('output/inputForSpoon.csv', 'w') as myFile:
    commitsCount = len(listOfCommitsToIterate)
    position = 1
    for key, value in listOfCommitsToIterate.items():
        if position != commitsCount:
            myFile.write(key + "," + ",".join(value) + "\n")
        else:
            myFile.write(key + "," + ",".join(value))
        position += 1
subprocess.call('./javaListMethods.groovy')
with open('output/outputOfSpoon.csv', 'r') as myFile:
    reader = csv.reader(myFile, delimiter='|')
    spoonOutput = list(reader)
dictOfSpoonOutput = dictionary_of_spoon_output(spoonOutput)
result = list()
for change in changes:
    oldCommitHash = change[0]
    newCommitHash = change[2]
    oldFilePath = change[1]
    newFilePath = change[3]
    commonMethods = [method for method in dictOfSpoonOutput[oldCommitHash][oldFilePath] if method in
                     dictOfSpoonOutput[newCommitHash][newFilePath]]
    for method in commonMethods:
        if dictOfSpoonOutput[oldCommitHash][oldFilePath][method] != \
                dictOfSpoonOutput[newCommitHash][newFilePath][method]:
            oldSignature = method+'#'+dictOfSpoonOutput[oldCommitHash][oldFilePath][method]
            newSignature = method+'#'+dictOfSpoonOutput[newCommitHash][newFilePath][method]
            result.append([newCommitHash, newFilePath, oldSignature, newSignature])
with open('output/finalReport.csv', 'w') as myFile:
    wr = csv.writer(myFile, delimiter='|')
    wr.writerows(result)
