from processors.simpleprops import SimplePropsProcessor

def test_simple_props():
    mol = {"atoms":[{"id":"a1","element":"C","x":0,"y":0}], "bonds":[]}
    p = SimplePropsProcessor()
    res = p.run(mol)
    assert res["atom_count"] == 1
    assert res["bond_count"] == 0
