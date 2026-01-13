# core/registry.py
from typing import Type, List, Optional
from .base_processor import BaseProcessor

_PROCESSORS: List[Type[BaseProcessor]] = []

def register(processor_cls: Type[BaseProcessor]):
    """Register a processor class."""
    _PROCESSORS.append(processor_cls)

def get_all() -> List[Type[BaseProcessor]]:
    """Return all registered processors."""
    return _PROCESSORS

def get_by_id(item_id) -> Optional[Type[BaseProcessor]]:
    """Return a registered processor class by its id attribute or None if not found.
    Adjust attribute access if your processors use a different identifier.
    """
    for proc in _PROCESSORS:
        # If processors are classes with a class attribute `id`
        if getattr(proc, "id", None) == item_id:
            return proc
        # If processors are instances stored in the registry, adapt accordingly
        # if hasattr(proc, "id") and proc.id == item_id:
        #     return proc
    return None

