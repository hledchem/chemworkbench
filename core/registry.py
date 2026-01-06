from typing import Type, List
from .base_processor import BaseProcessor

_PROCESSORS: List[Type[BaseProcessor]] = []

def register(processor_cls: Type[BaseProcessor]):
    """Register a processor class."""
    _PROCESSORS.append(processor_cls)

def get_all() -> List[Type[BaseProcessor]]:
    """Return all registered processors."""
    return _PROCESSORS
