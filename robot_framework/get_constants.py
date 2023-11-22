"""This module defines how the robot should receive and store constants/credentials from OpenOrchestrator."""

from dataclasses import dataclass

from OpenOrchestrator.orchestrator_connection.connection import OrchestratorConnection


@dataclass(kw_only=True)
class Constants:
    """An object for holding any robot specific constants. Expand as needed"""
    error_email: str


def get_constants(orchestrator_connection: OrchestratorConnection) -> Constants:
    """Get all constants used by the robot."""
    orchestrator_connection.log_trace("Getting constants.")

    constants = Constants(
        error_email = orchestrator_connection.get_constant("Error Email").value
    )

    return constants
