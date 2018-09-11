### Begin Coding Task 1

# Definition

You’re going to implement a program that mines a given Java GitHub code repository. The program analyses all the commits in that repository and finds commits that have added a parameter to an existing method. For example, assume that you have a method test(int x) in a Java file. If a commit changes this method to be test(int x, int y) then this commit added a parameter to this function.

The report should be a CSV file with columns  "Commit SHA, Java File, Old function signature, New function signature”. 

# Deliverables

* 1 GitHub repo that has all the code and scripts you used for this task

* The repo has a ReadMe file that tells me how to compile and run your code.

* The ReadMe should mention at least two repositories you already ran your code on

* Include the results of these two repositories in your repo


# Hints/Recommendations

* There are a lot of code analysis tools that can already find the changes between two versions of a Java file for you. There are also mining tools that can help you with this task.

* Try picking two popular Java Github repos that you can try this on so there’s a chance that you find the above type of changes.

### End Coding Task 1
