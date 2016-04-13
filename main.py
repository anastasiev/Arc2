from controllers.command_line_controller import CommandLineController
from services.controllerFactory import ControllerFactory

factory = ControllerFactory()
controller = factory.getController()
controller.navigation()
