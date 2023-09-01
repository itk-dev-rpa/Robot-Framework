from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from OpenOrchestratorConnection.orchestrator_connection import OrchestratorConnection

def initialize(orchestrator_connection:OrchestratorConnection) -> None:
    """Do all custom startup initializations of the robot."""
    pass