**AirBnB clone - The console**

This is the first step towards building our first full web application: the AirBnB clone. This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration...

Each task is linked and will help us to:
put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of our future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine

What is a command interpreter?

A command interpreter is a system software that understands and executes commands that are entered interactively by a human or from an another program.
Examples of command-line interpreters include DEC's DIGITAL Command Language (DCL) in OpenVMS and RSX-11, the various Unix shells (sh, ksh, csh, tcsh, zsh, Bash, etc.), CP/M's CCP, DOS' COMMAND.COM, as well as the OS/2 and the Windows CMD.
CMD like any other CLI shell has a prompt. The prompt conveys that the command interpreter is ready to take a command from the user. The default prompt of CMD is "~> ". A command is nothing but a set of instruction you want the command interpreter to perform. Pressing the return key(Enter) executes the command. After a command is executed, a new prompt is issued for accepting next command from the user.
