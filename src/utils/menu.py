from command import Command
from errors import ExitCommandException
from messages import Messages


class Menu:
    def __init__(self):
        self.commands = []

    def add_command(self, command: Command):
        self.commands.append(command)

    def execute(self):
        if not self.commands:
            print(Messages.NO_COMMANDS)
            return

        command_dict = {str(index + 1): command for index, command in
                        enumerate(self.commands)}

        while True:
            print(Messages.CHOOSE_COMMAND)
            for index, command in enumerate(self.commands):
                print(f"{index + 1}: {command.get_name()}")

            choice = input(Messages.COMMAND_PROMPT)

            try:
                command_dict[choice].execute()
            except KeyError:
                print(Messages.INVALID_SELECTION)
            except ExitCommandException:
                print(Messages.EXIT_MESSAGE)
                break
