# Meta HackerCup Utils

Contains a Jupyter Notebook to easily

- Create directories and files for each problem
- Move and unzip validation and final input files from your Downloads folder to the problem directory.
- Compile and run your C++ code against the input files.

A collection of scripts and utilities to streamline your workflow during the [Meta Hacker Cup](https://www.facebook.com/hackercup/) coding competition. This repository provides tools to automate the setup of problem directories, handle input files, compile your code, and run your solutions against validation and final inputs—all with minimal interaction required.

## Features

- **Automated Directory Setup**: Creates organized directories for each problem based on the year, round, and problem name.
- **Code Compilation**: Compiles your C++ code with customizable compilation arguments.
- **Input Handling**: Automatically moves or unzips validation and final input files from your Downloads folder.
- **Execution Automation**: Runs your compiled code against the input files and generates the appropriate output files.
- **Minimal Interaction**: Designed to let you focus on problem-solving rather than file management.

## Requirements

- **Operating System**: Any Unix-like environment.
- **Python**: Version 3.x.
- **C++ Compiler**: `g++` accessible via command line.
- **7-Zip**: Installable via `p7zip-full` package.
- **Jupyter Notebook**: For running the helper notebook.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/MetaHackerCupUtils.git
   cd MetaHackerCupUtils

2. Open helper.ipynb and replace the variables in the first cell with your own values.