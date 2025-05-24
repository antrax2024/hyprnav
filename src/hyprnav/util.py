"""
Utility Functions Module for HyprNav

This module provides common utility functions for the HyprNav application,
including logging, status display, file system operations, and command execution.
All functions use the Rich library for enhanced terminal output formatting.
"""

# - This is a Python 3.13 application
# - Enforce static typing (type hints) in all functions
# - Enable rich terminal output using `rich`
# - Manage Python dependencies and builds with `uv`
# - Adhere to PEP8 code style standards
# - Maintain English-only documentation and code comments
# - Apply camelCase convention for variables, methods and functions
# **Note**: While camelCase conflicts with PEP8's snake_case recommendation
# for Python, this requirement takes precedence per project specifications

import os
import subprocess
from rich.console import Console
from hyprnav.constants import SPACES_DEFAULT

# Initialize Rich console with custom log formatting
# Sets timestamp format and prevents time omission for repeated log entries
cl = Console(log_time_format="[%Y-%m-%d %H:%M:%S]")
cl._log_render.omit_repeated_times = False


def printLog(message: str) -> None:
    """
    Print a timestamped log message to the console.

    Uses Rich console logging to display messages with timestamps
    in the format [YYYY-MM-DD HH:MM:SS].

    Args:
        message: The log message to display
    """
    cl.log(message)


def printLine() -> None:
    """
    Print a decorative horizontal line separator.

    Displays 80 cyan-colored equal signs as a visual separator
    in the terminal output for better readability.
    """
    cl.print("[cyan]=[/cyan]" * 80)


def showStatus(preamble: str, message: str) -> None:
    """
    Display a formatted status message with a labeled preamble.

    Shows status information in a consistent format with a yellow-colored
    preamble label aligned to a fixed width, followed by the message content.

    Args:
        preamble: The status label (e.g., "LOADING", "PROCESSING")
        message: The status message content to display
    """
    cl.print(f"[bold yellow]{preamble:<{SPACES_DEFAULT}}[/bold yellow]: {message}")


def showError(message: str) -> None:
    """
    Display a formatted error message with red ERROR label.

    Shows error information in a consistent format with a red-colored
    "ERROR" label aligned to a fixed width, followed by the error message.

    Args:
        message: The error message content to display
    """
    error = "ERROR"
    cl.print(f"[bold red]{error:<{SPACES_DEFAULT}}[/bold red]: {message}")


def fileExists(file: str) -> bool:
    """
    Check if a file exists at the specified path.

    Uses os.path.isfile() to verify that the given path points to
    an existing regular file (not a directory or other file type).

    Args:
        file: The file path to check for existence

    Returns:
        True if the file exists and is a regular file, False otherwise
    """
    if os.path.isfile(file):
        return True
    else:
        return False


def configDirExists(configDir: str) -> bool:
    """
    Check if a directory exists at the specified path.

    Uses os.path.isdir() to verify that the given path points to
    an existing directory.

    Args:
        configDir: The directory path to check for existence

    Returns:
        True if the directory exists, False otherwise
    """
    if os.path.isdir(configDir):
        return True
    else:
        return False


def executeCommand(command: str) -> tuple[int, str, str]:
    """
    Execute a shell command and capture its output and error streams.

    Runs the specified command in a subprocess shell and captures both
    standard output and standard error. Returns all information needed
    to determine command success and process the results.

    Args:
        command: The shell command string to execute

    Returns:
        A tuple containing three elements:
        - int: The command's exit code (0 typically indicates success)
        - str: The standard output (stdout) from the command
        - str: The standard error (stderr) from the command

    Example:
        exit_code, output, error = executeCommand("ls -la")
        if exit_code == 0:
            print(f"Command succeeded: {output}")
        else:
            print(f"Command failed: {error}")
    """
    # Create subprocess with shell execution and pipe capture
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    # Wait for command completion and capture output streams
    stdout, stderr = process.communicate()
    # Return exit code and both output streams
    return process.returncode, stdout, stderr
