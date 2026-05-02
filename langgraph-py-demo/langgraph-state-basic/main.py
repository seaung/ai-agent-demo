import operator
from typing import Annotated, List, TypedDict

from langgraph.graph import StateGraph


class State(TypedDict):
    input: str
    all_action: Annotated[List[str], operator.add]
