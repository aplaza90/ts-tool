from utils.command import Command
from utils.errors import ExitCommandException


class AddSeriesCommand(Command):
    def execute(self):
        pass


class PerformOperationCommand(Command):
    def execute(self):
        """This class should guide the user to select the TS between the ones in
        the persistence layer and the operation to execute over it
        """
        pass


class ExitCommand(Command):
    def execute(self):
        print("Exiting the menu.")
        raise ExitCommandException()


