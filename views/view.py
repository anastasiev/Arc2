class ConsoleView(object):
    """
    Class shows info on console
    """


    def showMatches(self, matches):
        """
        Show list of match
        :param matches:
        :return:
        """
        for match in matches:
            print(match)

    def showMenu(self):
        """
        Show menu cases
        """
        print("""
        1. England
        2. Spain
        3. Ukraine
        4. Select team
        5. Add match
        6. Load matches from file
        7. Show all matches
        8. Exit
        """)

    def inputFromConsole(self):
        """
        Input from console
        :return:
        """
        return input()

    def printMessage(self, mes):
        print(mes)

