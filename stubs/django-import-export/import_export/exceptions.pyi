from typing import Any

class ImportExportError(Exception): ...
class FieldError(ImportExportError): ...

class ImportError(ImportExportError):
    error: Exception
    number: int | None
    row: dict[str, Any] | None
    def __init__(self, error: Exception, number: int | None = None, row: dict[str, Any] | None = None) -> None: ...
