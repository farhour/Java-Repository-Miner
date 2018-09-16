## Repository's Name

Epoxy: Epoxy is an Android library for building complex screens in a RecyclerView.

## Repository's Address

https://github.com/airbnb/epoxy

## The Latest Repository Change When Performing the Test

commit f84384fda86f5f608095d625206cfa096a850e04

## How to Clone

`git clone https://github.com/airbnb/epoxy.git ~/repository`

## FAQ
- **Which of these CVS files is the final result?**
  - The `finalReport.csv` file contains the final report. Every line of this file has `[Commit's hash, Path of Java file, Old method signature, New method signature]` format and indicates a method's signature modification in a Java file by a commit. The delimiter of this `CSV` file is the pipe character `(|)`.

- **What are the `CSV` files in this directory?**          
  - The `exceptionsOfSpoon.csv` file is made by the Groovy code and contains the generated exceptions of running the Spoon library for the Java files. For instance, if Spoon cannot process a Java file in a commit, then this exception is written to this file in `[commit's hash, Java file's path]` format for a further review.  
  - The `finalReport.csv` file contains the final report. Every line of this file has `[Commit's hash, Path of Java file, Old method signature, New method signature]` format and indicates a method's signature modification in a Java file by a commit. The delimiter of this `CSV` file is the pipe character `(|)`.
