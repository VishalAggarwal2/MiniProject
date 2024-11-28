import os
import random

# Directory to save Solidity files
os.makedirs("solidity_files", exist_ok=True)

# List of common errors to introduce
errors = [
    "function without visibility specifier",
    "state variable without initialization",
    "unprotected functions",
    "integer overflow",
    "unrestricted ether transfer",
    "use of deprecated functions",
    "arithmetic without safe checks",
]

# Example Solidity code snippets with intentional errors
solidity_snippets = [
    """
    pragma solidity ^0.8.0;
    contract TestContract {
        uint256 public counter; // No initialization
        function increase() {
            counter += 1; // No visibility
        }
    }
    """,
    """
    pragma solidity ^0.8.0;
    contract EtherTransfer {
        function sendEther(address payable recipient) public {
            recipient.transfer(address(this).balance); // Unrestricted transfer
        }
    }
    """,
    """
    pragma solidity ^0.8.0;
    contract Deprecated {
        function useCall() public {
            address(this).call(""); // Deprecated use of call
        }
    }
    """
]

# Generate 100 Solidity files with random errors
for i in range(1, 101):
    file_content = random.choice(solidity_snippets)
    file_name = f"solidity_files/Contract{i}.sol"
    with open(file_name, "w") as file:
        file.write(file_content)
