#!/usr/bin/env python3
"""
Script to generate PNG images from PlantUML diagram files
"""

import subprocess
import os
from pathlib import Path

def generate_puml_images():
    # Define the diagrams directory
    diagrams_dir = Path("/common/active/sblo/Dev/FinCom/docs/diagrams")
    
    # Create the diagrams directory if it doesn't exist
    diagrams_dir.mkdir(parents=True, exist_ok=True)
    
    # List of PlantUML files to convert
    puml_files = [
        "repository_structure.puml",
        "keyword_model.puml", 
        "ecs_model.puml",
        "constraint_model.puml",
        "metadata_model.puml",
        "relationships.puml",
        "processing_pipeline.puml",
        "business_context.puml"
    ]
    
    # Generate PNG images for each PlantUML file
    for puml_file in puml_files:
        puml_path = diagrams_dir / puml_file
        png_path = diagrams_dir / puml_file.replace(".puml", ".png")
        
        if puml_path.exists():
            try:
                # Run plantuml to generate PNG
                result = subprocess.run([
                    "plantuml", 
                    "-tpng",  # Generate PNG
                    str(puml_path),
                    "-o", str(diagrams_dir)  # Output directory
                ], capture_output=True, text=True, cwd=str(diagrams_dir.parent.parent))
                
                if result.returncode == 0:
                    print(f"✓ Generated {png_path.name}")
                else:
                    print(f"✗ Failed to generate {png_path.name}: {result.stderr}")
                    
            except FileNotFoundError:
                print("PlantUML not found. Please install PlantUML to generate diagrams.")
                break
            except Exception as e:
                print(f"✗ Error generating {png_path.name}: {str(e)}")
        else:
            print(f"✗ File not found: {puml_path}")

if __name__ == "__main__":
    generate_puml_images()