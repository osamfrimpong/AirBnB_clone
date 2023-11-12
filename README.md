# AirBnB Clone - The Console
## Description
ALX AirBnB Clone Software Engineer Project. This is the first stage in creating the AirBnB clone, your first complete web application. The reason this is a crucial initial step is that all subsequent projects will utilize the skills you develop during this one: Database storage, APIs, front-end integration, and HTML/CSS templating.
Functionalities of this command interpreter:

Create a new object (ex: a new User or a new Place)

Retrieve an object from a file, a database etc...

Do operations on objects (count, compute stats, etc...)

Update attributes of an object

Destroy an object

## Usage 
The console works both in interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt (hbnb) and waits for the user for input.

## File description
console.py - the console contains the entry point of the command interpreter. List of commands this console current supports:

EOF - exits console quit - exits console - overwrites default emptyline method and does nothing create - Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id destroy - Deletes an instance based on the class name and id (save the change into the JSON file). show - Prints the string representation of an instance based on the class name and id.

all - Prints all string representation of all instances based or not on the class name.

update - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

models/ directory contains classes used for this project: base_model.py - The BaseModel class from which future classes will be derived

## Testing
Unittests for the AirBnB project are outlined in the tests folder. To run the entire test suite simultaneously, execute the following command:

```
$ python3 unittest -m discover tests
```

You can also specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```

## AUTHORS
