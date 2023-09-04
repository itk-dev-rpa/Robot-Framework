from OpenOrchestratorConnection.orchestrator_connection import OrchestratorConnection

def reset(orchestrator_connection:OrchestratorConnection) -> None:
    """Clean up, close/kill all programs and start them again. """
    clean_up(orchestrator_connection)
    close_all(orchestrator_connection)
    kill_all(orchestrator_connection)
    open_all(orchestrator_connection)

def clean_up(orchestrator_connection:OrchestratorConnection) -> None:
    """Do any cleanup needed to leave a blank slate."""
    pass

def close_all(orchestrator_connection:OrchestratorConnection) -> None:
    """Gracefully close all applications used by the robot."""
    pass

def kill_all(orchestrator_connection:OrchestratorConnection) -> None:
    """Forcefully close all applications used by the robot."""
    pass

def open_all(orchestrator_connection:OrchestratorConnection) -> None:
    """Open all programs used by the robot."""
    pass