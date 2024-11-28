import os
import subprocess
import json

# Directory to save Mythril analysis results
os.makedirs("mythril_results", exist_ok=True)

solidity_files = [f for f in os.listdir("solidity_files") if f.endswith(".sol")]

# Analyze each Solidity file with Mythril and save the results
for file in solidity_files:
    file_path = os.path.join("solidity_files", file)
    output_file = os.path.join("mythril_results", f"{file}.json")
    command = f"myth analyze {file_path} -o json > {output_file}"
    subprocess.run(command, shell=True)
