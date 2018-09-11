import sys
from pydriller import RepositoryMining
import csv

countOfArgs = len(sys.argv)
pathToRepo = None
if countOfArgs == 2:
    pathToRepo = sys.argv[1]
else:
    pathToRepo = '../repository/'
changes = []
for commit in RepositoryMining(pathToRepo, only_modifications_with_file_types=['.java']).traverse_commits():
        for modification in commit.modifications:
            if modification.change_type is not None:
                extOfFile = modification.filename[modification.filename.find('.') + 1:]
                if extOfFile == 'java' and modification.change_type.name == 'MODIFY':
                    changes.append([commit.parents[0], modification.old_path, commit.hash, modification.new_path])
with open('output/changes.csv', 'w') as myFile:
    wr = csv.writer(myFile)
    wr.writerows(changes)
