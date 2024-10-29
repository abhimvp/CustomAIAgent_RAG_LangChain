"""
Another tool to save notes in a text file by the agent
"""
# Make tools out of functions, can be used with or without arguments
# from langchain.agents import tool

# @tool
# def note_tool(note):
#     """
#     Tool to save notes in a local text file
#     Args:
#         note (str): The text note to be save
#     """
#     with open("notes.txt", "a") as f: # a means append mode
#         f.write(note + "\n")
# note_tool.type="function"
"""
Another tool to save notes in a text file by the agent
"""
from langchain.tools import StructuredTool
from typing import Optional

def note_tool(note: str) -> str:
    """
    Tool to save notes in a local text file
    Args:
        note (str): The text note to be saved
    Returns:
        str: A confirmation message
    """
    with open("notes.txt", "a") as f: # a means append mode
        f.write(note + "\n")
    return "Note saved successfully"

# Create the StructuredTool with all necessary information
note_tool_1 = StructuredTool.from_function(
    func=note_tool,
    name="note_tool",
    description="Tool to save notes in a local text file",
    return_direct=False,
    args_schema=None,
)
