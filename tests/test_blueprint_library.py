import os
import pytest
import shutil

# TDD: Test if the blueprint library structure is correct
def test_python_developer_blueprint_exists():
    blueprint_path = "agents/python-developer"
    assert os.path.isdir(blueprint_path)
    assert os.path.exists(os.path.join(blueprint_path, "AGENTS.md"))
    assert os.path.exists(os.path.join(blueprint_path, "TOOLS.md"))
    assert os.path.isdir(os.path.join(blueprint_path, "engrams"))

def test_blueprint_manifest_load():
    manifest_path = "agents/python-developer/manifest.json"
    assert os.path.exists(manifest_path)
    
    import json
    with open(manifest_path, "r") as f:
        manifest = json.load(f)
        
    assert "name" in manifest
    assert "version" in manifest
    assert manifest["name"] == "Python Developer"

