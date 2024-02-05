# **Airbnb- console**

As part of the AirBnB project at Holberton School, the console represents the initial phase dedicated to fundamental higher-level programming concepts. The ultimate goal of the AirBnB project is to successfully deploy a server emulating the essential features of the AirBnB Website (HBnB). In this specific phase, the focus is on creating a command interpreter to effectively manage objects for the AirBnB websit.

## Features

## Command Interpreter
## Description
The Command Interpreter is used to manage the whole application's functionality from the command line, such as:

- **Create a new object.**
- **Retrieve an object from a file, database, etc.**
- **Execute operation on objects. e.g. Count, compute statistics, etc.**
- **Update object's attributes.**
-**Destroy an object.**

## Usage

- To launch the console application in interactive mode simply run:

 **console.py**

- or to use the non-interactive mode run:

 **echo "your-command-goes-here" | ./console.py**

## Commands
In order to give commands to the console, these will need to be piped through an echo in case of Non-interactive mode.

In Interactive Mode the commands will need to be written with a keyboard when the prompt appears and will be recognized when an enter key is pressed (new line). As soon as this happens, the console will attempt to execute the command through several means or will show an error message if the command didn't run successfully. In this mode, the console can be exited using the CTRL + D combination, CTRL + C, or the command quit or EOF.

## Tests
If you wish to run at the test for this application all of the test are located under the test/ folder and can execute all of them by simply running:

**python3 -m unit**	
