import os
import tempfile
import shutil
import sys
import pytest

# Since the codebase is modular, we can import find_aim_root from one of the files.
# Let's use src.config_utils as the representative implementation.
from src.config_utils import find_aim_root

def test_find_aim_root_with_setup_sh():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a mock deep directory structure
        deep_dir = os.path.join(temp_dir, "nested", "deep", "dir")
        os.makedirs(deep_dir)
        
        # Create setup.sh at the root of temp_dir
        open(os.path.join(temp_dir, "setup.sh"), 'a').close()
        
        # Change current working directory to the deep directory
        original_cwd = os.getcwd()
        os.chdir(deep_dir)
        
        try:
            # find_aim_root should traverse up and find temp_dir via setup.sh
            found_root = find_aim_root()
            assert found_root == temp_dir
        finally:
            os.chdir(original_cwd)

def test_find_aim_root_with_core_config():
    with tempfile.TemporaryDirectory() as temp_dir:
        deep_dir = os.path.join(temp_dir, "nested", "deep", "dir")
        core_dir = os.path.join(temp_dir, "core")
        os.makedirs(deep_dir)
        os.makedirs(core_dir)
        
        # Create core/CONFIG.json at the root of temp_dir
        open(os.path.join(core_dir, "CONFIG.json"), 'a').close()
        
        original_cwd = os.getcwd()
        os.chdir(deep_dir)
        
        try:
            # find_aim_root should traverse up and find temp_dir via core/CONFIG.json
            found_root = find_aim_root()
            assert found_root == temp_dir
        finally:
            os.chdir(original_cwd)
