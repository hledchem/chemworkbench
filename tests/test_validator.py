from core.validator import validate_molecule

def test_valid_molecule():
    mol = {"atoms":[{"id":"a1","element":"C","x":0,"y":0}], "bonds":[]}
    validate_molecule(mol)

def test_invalid_molecule():
    mol = {"atoms":[{"element":"C","x":0,"y":0}], "bonds":[]}
    import pytest
    with pytest.raises(ValueError):
        validate_molecule(mol)
