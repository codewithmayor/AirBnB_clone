#!/usr/bin/python3
"""Console Entry Point"""
import cmd
import os
from models import storage, classes
import re


class HBNBCommand(cmd.Cmd):
    """Command Interpreter class
    """
    prompt = "(hbnb) "

    # def preloop(self) -> None:
    #     """Add newline character to prompt if interpreter is
    #     run in non-interactive mode
    #     """
    #     if not os.isatty(self.stdin.fileno()):
    #         self.prompt = ""

    def do_EOF(self, line):
        """EOF command to exit program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit program
        """
        return True

    def emptyline(self) -> bool:
        """Does nothing when emptyline is enter
        as a command
        """
        pass

    def do_create(self, line):
        """Create an instance of the specified model and
            save it to file storage
        """
        # Print error if empty string is supplied
        if line == "":
            print("** class name missing **")
            return

        # Create and save new instance of class
        if line in classes:
            base = classes[line]()
            base.save()
            print(base.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of instance based
            on the class name and id
        """
        obj = find_object(line)

        if obj is None:
            return

        print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on
        its class name and id
        """

        obj = find_object(line)

        if obj is None:
            return

        key = f"{obj.__class__.__name__}.{obj.id}"

        objects = storage.all()
        del objects[key]
        del obj

        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name.
        """
        # No argument print all instances
        if line == "":
            for obj in storage.all().values():
                print(obj)
            return

        t_class = get_class(line)

        if t_class is None:
            print("** class doesn't exist **")
            return

        for obj in storage.all().values():
            # Print objects that match the class name
            if obj.__class__.__name__ == t_class.__name__:
                print(obj)

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        """
        obj = find_object(line)

        if obj is None:
            return

        args = parse_args(line)

        if len(args) >= 4:
            # Update object attribute
            obj.__setattr__(args[2], args[3])
            obj.save()
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")

    def do_count(self, line):
        """Count command counts the number of instances
        of a class
        """
        # No argument
        if line == "":
            # Return total number of objects
            print(len(storage.all().values()))
            return

        t_class = get_class(line)
        if t_class is None:
            print("** class doesn't exist **")
            return

        # Count number of matching instancess
        matching_objs = [obj for obj in storage.all().values() if type(
            obj).__name__ == t_class.__name__]

        print(len(matching_objs))

    def complete_all(self, text, *args):
        """Completion for all command"""
        return autocomplete_class(text)

    def complete_show(self, text, line, *args):
        """Completion for show command"""
        return autocomplete_class_and_id(text, line)

    def complete_create(self, text, *args):
        """Completion for create command"""
        return autocomplete_class(text)

    def complete_count(self, text, *args):
        """Completion for create command"""
        return autocomplete_class(text)

    def complete_destroy(self, text, line, *args):
        """Completion for destroy command"""
        return autocomplete_class_and_id(text, line)

    def complete_update(self, text, line, *args):
        """Completion for update command"""
        return autocomplete_class_and_id(text, line)


def parse_args(line):
    """Parses the command line argument and
    returns a tuple of all the arguments
    """
    args = re.findall(r'[^"\s]+|"[^"]+"', line)
    return tuple([arg.replace('"', "") for arg in args])


def get_class(class_name):
    """Returns the class associated with
     the class_name or None if it doesn't exist
    """
    return classes.get(class_name)


def get_object(cls, id):
    """Retrieves an object from file storage based on
    its class and id
    """
    key = f"{cls.__name__}.{id}"
    objects = storage.all()
    return objects.get(key)


def find_object(line):
    """Retrieves an object based on className and id and handles
    error printing. Returns the matching object or None
    """
    args = parse_args(line)

    if len(args) == 0:
        print("** class name missing **")
        return None

    t_class = get_class(args[0])

    if t_class is None:
        print("** class doesn't exist **")
        return None

    if len(args) == 1:
        print("** instance id missing **")
        return None

    obj = get_object(t_class, args[1])

    if obj is None:
        print("** no instance found **")
        return None

    return obj


def autocomplete_class_and_id(text, line):
    """Autocompletion for commands with
    class and id positional arguments
    """
    args = parse_args(line)

    if not text:
        if len(args) == 1:
            return list(classes.keys())
        elif len(args) == 2:
            # Return ids of all objects based on class
            return [obj.id for obj in storage.all().values()
                    if type(obj).__name__ == args[1]]
    else:
        # Handle positional parameters
        if len(args) == 2:
            return [class_name for class_name in classes.keys()
                    if class_name.startswith(text)]
        elif len(args) == 3:
            return [obj.id for obj in storage.all().values()
                    if type(obj).__name__ == args[1]
                    and obj.id.startswith(text)]


def autocomplete_class(text):
    """AutoCompletion for commands with
    class positional argument
    """
    if not text:
        return list(classes.keys())
    else:
        return [c_name for c_name in classes.keys()
                if c_name.startswith(text)]


if __name__ == "__main__":
    HBNBCommand().cmdloop()
