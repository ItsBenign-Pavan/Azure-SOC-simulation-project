#!/usr/bin/env python3
"""
Azure SOC Project Architecture Flowchart Generator
Converts Mermaid diagram to PNG using mermaid-cli
"""

import subprocess
import os
import sys

def generate_flowchart_png():
    """Generate PNG flowchart from Mermaid markdown"""
    
    # Input and output paths
    input_file = "architecture-flowchart.md"
    output_file = "azure-soc-architecture-flowchart.png"
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found!")
        sys.exit(1)
    
    print("🔄 Generating PNG flowchart from Mermaid diagram...")
    print(f"📄 Input: {input_file}")
    print(f"🖼️  Output: {output_file}")
    
    try:
        # Check if mmdc (mermaid-cli) is installed
        subprocess.run(["mmdc", "--version"], capture_output=True, check=True)
        
        # Generate PNG with high quality
        command = [
            "mmdc",
            "-i", input_file,
            "-o", output_file,
            "-b", "white",
            "-s", "2"
        ]
        
        subprocess.run(command, check=True)
        print(f"✅ Successfully generated {output_file}")
        print(f"📊 Flowchart dimensions: High-resolution PNG")
        
    except FileNotFoundError:
        print("❌ mermaid-cli not installed!")
        print("\n📦 Installation Instructions:")
        print("   npm install -g @mermaid-js/mermaid-cli")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error generating PNG: {e}")
        sys.exit(1)

if __name__ == "__main__":
    generate_flowchart_png()
