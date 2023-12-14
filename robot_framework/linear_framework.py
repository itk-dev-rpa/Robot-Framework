"""This module is the primary module of the robot framework. It collects the functionality of the rest of the framework."""

# This module is not meant to exist next to queue_framework.py in production:
# pylint: disable=duplicate-code

import sys

from OpenOrchestrator.orchestrator_connection.connection import OrchestratorConnection

from robot_framework import initialize
from robot_framework import reset
from robot_framework.exceptions import BusinessError, handle_error, log_exception
from robot_framework import process
from robot_framework import config


def main():
    """The entry point for the framework. Should be called as the first thing when running the robot."""
    orchestrator_connection = OrchestratorConnection.create_connection_from_args()
    sys.excepthook = log_exception(orchestrator_connection)

    orchestrator_connection.log_trace("Robot Framework started.")
    initialize.initialize(orchestrator_connection)

    error_count = 0
    for _ in range(config.MAX_RETRY_COUNT):
        try:
            reset.reset(orchestrator_connection)
            process.process(orchestrator_connection)
            break

        # If any business rules are broken the robot should stop entirely.
        except BusinessError as error:
            handle_error("Business Error", error, None, orchestrator_connection)
            break

        # We actually want to catch all exceptions possible here.
        # pylint: disable-next = broad-exception-caught
        except Exception as error:
            error_count += 1
            handle_error(f"Process Error #{error_count}", error, None, orchestrator_connection)

    reset.clean_up(orchestrator_connection)
    reset.close_all(orchestrator_connection)
    reset.kill_all(orchestrator_connection)

    if config.FAIL_ROBOT_ON_TOO_MANY_ERRORS and error_count == config.MAX_RETRY_COUNT:
        raise RuntimeError("Process failed too many times.")
