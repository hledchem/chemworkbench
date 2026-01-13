import json
from jsonschema import validate, ValidationError
from pathlib import Path

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schema" / "molecule.json"

def validate_molecule(mol_json: dict) -> None:
    schema = json.loads(SCHEMA_PATH.read_text())
    try:
        validate(instance=mol_json, schema=schema)
    except ValidationError as e:
        raise ValueError(f"Invalid molecule JSON: {e.message}")
