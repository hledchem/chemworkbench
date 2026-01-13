from core.base_processor import Processor
from typing import Dict, Any

class SimplePropsProcessor(Processor):
    def run(self, molecule: Dict[str, Any]) -> Dict[str, Any]:
        atom_count = len(molecule.get("atoms", []))
        bond_count = len(molecule.get("bonds", []))
        return {"atom_count": atom_count, "bond_count": bond_count}
