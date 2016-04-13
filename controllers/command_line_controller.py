import sys

from controllers.base_controller import Controller
from services.matchFactory import MatchFactory
from services.matchesService import MatchesService
from views.view import ConsoleView


class CommandLineController(Controller):

    def navigation(self):
        serialyser = self._getSerialiseMethod()
        matches = serialyser.loadMatches()
        if sys.argv[1] == "-p":
            self.view.showMatches(matches)
        elif sys.argv[1] == "-a":
            self.service.addMatch(matches)
            serialyser.saveMatches(matches)
        else:
            self.view.printMessage("Unknown command")
