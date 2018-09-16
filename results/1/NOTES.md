## Repository's Name

OkHttp: An HTTP+HTTP/2 client for Android and Java applications.

## Repository's Address

https://github.com/square/okhttp

## The Latest Repository Change When Performing the Test

commit 0ad4130a085e04d368df02b83707f5ecbae8f076

## How to Clone

`git clone https://github.com/square/okhttp.git ~/repository`

## FAQ
- **Which of these CVS files is the final result?**
  - The `finalReport.csv` file contains the final report. Every line of this file has `[Commit's hash, Path of Java file, Old method signature, New method signature]` format and indicates a method's signature modification in a Java file by a commit. The delimiter of this `CSV` file is the pipe character `(|)`.

- **What are the `CSV` files in this directory?**          
  - The `exceptionsOfSpoon.csv` file is made by the Groovy code and contains the generated exceptions of running the Spoon library for the Java files. For instance, if Spoon cannot process a Java file in a commit, then this exception is written to this file in `[commit's hash, Java file's path]` format for a further review.  
  - The `finalReport.csv` file contains the final report. Every line of this file has `[Commit's hash, Path of Java file, Old method signature, New method signature]` format and indicates a method's signature modification in a Java file by a commit. The delimiter of this `CSV` file is the pipe character `(|)`.
