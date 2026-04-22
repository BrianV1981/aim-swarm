#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys

def create_template(role_name):
    return f"""# SWARM ROLE: {role_name.upper()} SPECIALIST

## PRIMARY DIRECTIVE
You are a highly specialized {role_name.title()} Engineer operating as a sub-agent within the A.I.M. Swarm architecture.
Your sole focus is the {role_name} layer and tasks related to it.

## OPERATING RULES
1. **Isolation:** You operate strictly within this isolated node directory.
2. **Autonomy:** Do not modify files outside your node.
3. **Communication:** When you finish a task, or if you are blocked, clearly state your status in your chat so the Orchestrator (A.I.M.) can read it.
"""

def main():
    parser = argparse.ArgumentParser(description="Scaffold a new Sovereign Node for the A.I.M. Swarm.")
    parser.add_argument("role_name", type=str, help="The role/persona for the new agent (e.g., 'frontend', 'database').")
    parser.add_argument("--output_dir", type=str, help="Optional custom output directory. Defaults to 'teams/<role_name>_node/'.")
    
    args = parser.parse_args()
    role_name = args.role_name
    
    if args.output_dir:
        node_dir = args.output_dir
    else:
        node_dir = os.path.join("teams", f"{role_name}_node")
        
    continuity_dir = os.path.join(node_dir, "continuity")
    gemini_md_path = os.path.join(node_dir, "GEMINI.md")
    
    # 1. Directory Scaffolding
    try:
        os.makedirs(continuity_dir, exist_ok=True)
        print(f"Created directories for {node_dir}")
    except OSError as e:
        print(f"Error creating directories: {e}")
        sys.exit(1)
        
    # 2. Template Generation
    try:
        with open(gemini_md_path, "w") as f:
            f.write(create_template(role_name))
        print(f"Generated {gemini_md_path}")
    except OSError as e:
        print(f"Error writing GEMINI.md: {e}")
        sys.exit(1)
        
    # 3. Git Initialization
    try:
        subprocess.run(["git", "init"], cwd=node_dir, check=True, capture_output=True)
        print(f"Initialized isolated git repository in {node_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error initializing git repository: {e.stderr.decode('utf-8')}")
        sys.exit(1)
        
    print(f"Successfully scaffolded Sovereign Node: {role_name} at {node_dir}")

if __name__ == "__main__":
    main()
