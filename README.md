<a href="https://github.com/farhour/Java-Sample-Repository" target="_blank"><img src="http://blog.inf.ed.ac.uk/sapm/files/2014/02/img.jpg" title="Java Repository Miner" alt="Java Repository Miner"></a>

# Coding Task 1 - Java Repository Miner

This repository is mostly an **academic exercise**. This code solves the problem of finding all modified signatures of Java methods in a given repository. This code uses [PyDriller](https://github.com/ishepard/pydriller) package to traverse all the commits in a repository and find ones with at least one modified file with Java extension. By traversing the commits through Git and using the [Spoon](https://github.com/INRIA/spoon) library, all signatures of modified Java files are made for analyzing in the final step. The full explanation of the problem can be found in `TASK.md` in this repo. For more details about the code, see the [FAQ](#faq) section.

---

## Table of Contents

- [Example](#example)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [FAQ](#faq)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

---

## Example

Assume that you have a method `test(int x)` in a Java file. If a commit changes this method to be `test(int x, int y)` then this commit adds a parameter to this method.
The report should be a `CSV` file with columns  `"Commit's hash, Path of Java file, Old method signature, New method signature"`.

---

## Requirements

This project is fully written in **Python 3** and **Groovy 2.4**. To clone this repo and run the program, you need:
* **Git** (1.7.x or newer)
* **Python** (3.2 or above)
* **PIP Package manager**
* **Java** (10.0 or above)
* **Groovy** (2.4 or above)

**Note that Git is required for running the main code because the Groovy part of the program executes Git commands to traverse through the commits of given repository.**

---

## Installation

### Installation on Ubuntu 16.04

- **Updating source list and installed packages:**
```shell
$ sudo apt-get update
$ sudo apt-get upgrade
```

- **Installing Java Development Kit (JDK):**
```shell
$ sudo apt-get install default-jdk
```
**Checking the installation:**
```shell
$ java -version
		OpenJDK Runtime Environment (build 1.8.0_181-8u181-b13-0ubuntu0.16.04.1-b13)
		OpenJDK 64-Bit Server VM (build 25.181-b13, mixed mode)
$ javac -version
		javac 1.8.0_181
```

- **Installing Groovy**
```shell
$ sudo apt-get install groovy2
```
**Checking the installation:**
```shell
$ groovy -v
		Groovy Version: 2.4.5 JVM: 1.8.0_181 Vendor: Oracle Corporation OS: Linux
```

- **Installing Python 3, pip, and venv:**
```shell
$ sudo apt-get install python3 python3-pip python3-venv
```
**Checking the installation:**
```shell
$ python3 -V
		Python 3.5.2
$ pip3 -V
		pip 8.1.1 from /usr/lib/python3/dist-packages (python 3.5)
```

- **Installing Git:**
```shell
$ sudo apt-get install git-core
```
**Checking the installation:**
```shell
$ git --version
		git version 2.7.4
```

- **Cloning the repository and preparing for the first run:**
**DO NOT FORGET** to grant the owner of `javaListMethods.groovy` file execution permissions. It is necessary to run the code.
**DO NOT FORGET** to install the requirements using the pip package manager.
```shell
$ git clone https://github.com/farhour/Java-Repository-Miner.git miner
$ cd miner
$ chmod u+x javaListMethods.groovy
$ python3 -m venv my_env
$ source my_env/bin/activate
$ pip install -r requirements.txt
```

- **Cloning a sample Java repository and running the code:**
**DO NOT FORGET** to clone the sample repository in a directory separate from the program's directory because it is a different repository to traverse.
```shell
$ git clone https://github.com/farhour/Java-Sample-Repository.git ../sample-repository
$ python run.py ../sample-repository
```

- **Viewing the final result:**
**The delimiter of this `CSV` file is the pipe character `(|)`.**
```shell
$ cat output/finalReport.csv
```

### Installation on Mac OS X

**Follow the steps in the previous section but run the commands in Mac OS X.**

**DO NOT FORGET** to grant the owner of `javaListMethods.groovy` file execution permissions. It is necessary to run the code.

**DO NOT FORGET** to install the requirements using the pip package manager.

**DO NOT FORGET** to clone the sample repository in a directory separate from the program's directory because it is a different repository to traverse.

---

## Usage

**After installing the requirements in the previous section, you have two options to run the program:**

**Option 1**: Input the path of the repository through the command line. This repository must be in a directory separate from the program's directory. The result in `CSV` format will be created in the output directory as `finalReport.csv`. The delimiter of this `CSV` file is the pipe character `(|)`.
```shell
$ python run.py /path/to/repository/
```
**Option 2**: Specify the path of the repository in the `run.py` file and then run it. The result in `CSV` format will be created in the output directory as `finalReport.csv`. The delimiter of this `CSV` file is the pipe character `(|)`.
```python
pathToRepo = '../repository/'
```
```shell
$ python run.py
```

---

## Features

- Using [PyDriller package](https://github.com/ishepard/pydriller) to mine the given repository and find all Java modified files in the commits.
- Using the [Spoon library](https://github.com/INRIA/spoon) to analyze the modified Java files and create signatures of their methods.
- Reporting the exceptions of the Spoon analyzer in a separate file named `exceptionsOfSpoon.csv` without stopping the main code.
- Generating the result in `CSV` format named `finalReport.csv`.

---

## FAQ

- **What are the `CSV` files created in the output folder?**
    - The `pathToRepo.csv` file is created by the program and contains the path of given repository.
    - Every line in the `changes.csv` file has `[parent commit's hash, parent Java file's path, new commit's hash, new Java file's path]` format and indicates a modification in a single java file by a commit.
    - The `inputForSpoon.csv` file is made from the `changes.csv` file by the program and has `[commit's hash, Java file's path [, Java file's path... ]]` format. This file is used by the Groovy code to create the signatures of Java files in the given commits.
    - The `outputOfSpoon.csv` file is made by the Groovy code and has `[commit's hash, Java file's path, signatures of the Java file's methods]` format. This file will be used by the main program to find the modified signatures between the commits.
    - The `exceptionsOfSpoon.csv` file is made by the Groovy code and contains the generated exceptions of running the Spoon library for the Java files. For instance, if Spoon cannot process a Java file in a commit, then this exception is written to this file in `[commit's hash, Java file's path]` format for a further review.
    - The `finalReport.csv` file contains the final report. Every line of this file has `[Commit's hash, Path of Java file, Old method signature, New method signature]` format and indicates a method's signature modification in a Java file by a commit. The delimiter of this `CSV` file is the pipe character `(|)`.

- **Why do you run the Spoon analyzer in a Try-Catch block?**
    - Maybe a Java file does not have a correct structure to be faultlessly processed by Spoon. In addition to this, perhaps the Spoon library has a bug itself for handling a Java file. So, creating a separate file to split the exceptions and avoid stopping the program execution is a proper idea.

- **Why do you grant the owner of `javaListMethods.groovy` file execution permissions?**
    - We grant the execution permission to the owner of `javaListMethods.groovy` because it should always be run with bash.

---

## Contributing

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine.

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request.

---

## Support

Reach out to me at one of the following places!

- Website at <a href="https://farhour.com" target="_blank">farhour.com</a>
- Twitter at <a href="http://twitter.com/farhour" target="_blank">@farhour</a>

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- This project is licensed under the **[MIT license](http://opensource.org/licenses/mit-license.php)**.
- Copyright © 2018 <a href="https://farhour.com" target="_blank">**Farbod Farhour**</a>

---

This README was written with ❤️.
