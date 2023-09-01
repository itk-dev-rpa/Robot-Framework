from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from OpenOrchestratorConnection.orchestrator_connection import OrchestratorConnection

def get_constants(orchestrator_connection:OrchestratorConnection) -> dict:
    """Get all constants used by the robot."""
    constants = {}

    # constant = orchestrator_connection.get_constant("name")
    # constants["name"] = constant

    return constants