from typing import Any, Callable, Dict, List, Union, Pattern

class IdNotFoundError(Exception):
    """Exception raised if id not found.

    Attributes:
        pk -- primary key / id
    """

    def __init__(self, pk: int) -> None:
        self.pk = pk

    def __str__(self) -> str:
        return f"Id {self.pk!r} does not exist in the JSON db"


class DataNotFoundError(Exception):
    """Exception raised if id not found.

    Attributes:
        data
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        self.data = data

    def __str__(self) -> str:
        return f"The data {self.data!r} does not exists in JSON db"

class SchemaError(Exception):
    """Exception raised for field/key errors."""

    def __init__(self, *args) -> None:
        self.args = args

    def __str__(self) -> str:
        return str(self.args)
