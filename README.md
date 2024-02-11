# 0x00 - AirBnB clone - The console


## Description of the project

This is a team work project called "AirBnB_clone". AUTHORS:
- Mojalefa Kodisang
- Habiba Zguaid

The console is the first step towards building a full web application: the AirBnB clone.
The console built during this project will be used with all other following projects o fthe AirBnB clone: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help to:

- put in place a parent class (called BaseModel) to take care of the initialization,
  serialization and - - - - deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## Description of the command interpter:

### How to start the command interpreter:

- Execute console `./console.py`
- Commands:

  - EOF : To Exit The program
  - quit : To Exit The program
  - help : to see The command line.
  - `Enter + empty line ` : shouldn’t execute anything

### How to use the command interpreter:

- create: to Creates a new instance
  Usage: `create <name Class>` it will give you your id.

- show: to Prints the string representation of an instance based on the class name and id.
  Usage: `show <name Class> <id>`.

- destroy: Deletes an instance based on the class name and id
  Usage: `destroy <name Class> <id>`

- all: Prints all string representation of all instances based or not on the class name.
  Usage: `all <name Class>` or `all`.

- update: Updates an instance based on the class name and id by adding or updating attribute
  Usage: `update <class.__name__> <id> <key> <value>`

### Examples:

- create command:
create BaseModel

- show command:
show <cass.__name__> <id>

- destroy command:
destroy <class.__name__> <id>

- all command:
all or all <class.__name__>

- update command:
update <class.__name__> <id> <key> <value>
