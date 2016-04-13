import unittest

from controllers.command_line_controller import CommandLineController
from controllers.controller import MatchesController
from serialysers.jsonSerialyser import JsonSerialyser
from serialysers.yamlSerialyser import YamlSerialyser
from services.matchFactory import MatchFactory
from tests.string_support import *


class TestStringMethods(unittest.TestCase):

    def test_json(self):
        serialyser = JsonSerialyser()
        service = MatchFactory()
        m = service.getAllMatches()
        serialyser.saveMatches(m)

    def test_config(self):
        controller = MatchesController()
        obj = controller._getSerialiseMethod()
        res = isinstance(obj, JsonSerialyser)
        self.assertEqual(res, True, "OK")


    def test_json_serialise(self):
        JsonSerialyser().saveMatches(MatchFactory().getAllMatches())
        strIO = getStringFromSerialyser()
        strIO.seek(0)
        with open("matches.json", "rt") as f:
            for line in f:
                self.assertEqual(strIO.readline(), line)

    def test_yaml_serialise(self):
        YamlSerialyser().saveMatches(MatchFactory().getAllMatches())
        strIO = getStringFromSerialyser("matches.yaml")
        strIO.seek(0)
        with open("matches.yaml", "rt") as f:
            for line in f:
                self.assertEqual(strIO.readline(), line)

    def test_teamPrint(self):
        matches = MatchFactory().getAllMatches()
        print(matches[0])
        self.assertTrue(matches[0].equal(matches[0]))

    def test_controller(self):
        contr = CommandLineController()
        contr.navigation()




if __name__ == '__main__':
    unittest.main()