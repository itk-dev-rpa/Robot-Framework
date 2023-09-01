import traceback
import sys

from OpenOrchestratorConnection.orchestrator_connection import OrchestratorConnection

import initialize
import get_constants
import reset
from process import process

def main():
    orchestrator_connection = OrchestratorConnection.create_connection_from_args()
    sys.excepthook = log_exception(orchestrator_connection)

    orchestrator_connection.log_trace("Process started.")

    orchestrator_connection.log_trace("Initialzing.")
    initialize.initialize(orchestrator_connection)

    orchestrator_connection.log_trace("Getting constants.")
    constants = get_constants.get_constants(orchestrator_connection)


    error_count = 0
    max_retry_count = 3
    for _ in range(max_retry_count):
        try:
            orchestrator_connection.log_trace("Resetting.")
            reset.reset(orchestrator_connection)

            orchestrator_connection.log_trace("Running process.")
            process(orchestrator_connection)

            break

        except BusinessError as error:
            orchestrator_connection.log_error(f"BusinessError: {error}\nTrace: {traceback.format_exc()}")
            break

        except Exception as error:
            error_count += 1
            error_type = type(error).__name__
            orchestrator_connection.log_error(f"Error caught during process. Number of errors caught: {error_count}. {error_type}: {error}\nTrace: {traceback.format_exc()}")
    
    reset.clean_up()
    reset.close_all()
    reset.kill_all()


def log_exception(orchestrator_connection:OrchestratorConnection) -> callable:
    def inner(type, value, traceback):
        orchestrator_connection.log_error(f"Type: {type}\nValue: {value}\nTrace: {traceback}")
    return inner


class BusinessError(Exception):
    pass


if __name__ == '__main__':
    main()