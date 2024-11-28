import os
import random

# Create a directory to store generated files
os.makedirs("solidity_files", exist_ok=True)

# List of common errors or vulnerabilities to introduce
errors = [
    "Reentrancy", "Integer Overflow", "Unchecked Return Value", "DoS with Gas Limit",
    "Access Control Issues", "Deprecated Functions", "tx.origin Authorization",
    "Timestamp Dependence", "Transaction Ordering Dependence", "Selfdestruct Vulnerability"
]

# Base contract templates
base_contracts = [
    """
    // Safe contract example
    pragma solidity ^0.8.0;
    contract SafeContract {{
        uint public balance;
        function deposit() public payable {{
            balance += msg.value;
        }}
        function withdraw(uint amount) public {{
            require(balance >= amount, "Insufficient balance");
            payable(msg.sender).transfer(amount);
            balance -= amount;
        }}
    }}
    """,
    """
    // Simple storage contract
    pragma solidity ^0.8.0;
    contract SimpleStorage {{
        uint storedData;
        function set(uint x) public {{
            storedData = x;
        }}
        function get() public view returns (uint) {{
            return storedData;
        }}
    }}
    """,
    """
    // Example with fallback
    pragma solidity ^0.8.0;
    contract FallbackExample {{
        event Log(string message);
        fallback() external payable {{
            emit Log("Fallback called");
        }}
    }}
    """
]

# Function to introduce errors into a base contract
def introduce_error(contract, error_type):
    if error_type == "Reentrancy":
        return contract.replace(
            "function withdraw(uint amount) public {",
            "function withdraw(uint amount) public {\n    (bool success, ) = msg.sender.call{value: amount}(\"\");\n    require(success);\n"
        )
    elif error_type == "Integer Overflow":
        return contract.replace(
            "balance += msg.value;",
            "balance = balance + 1;"
        )
    elif error_type == "Unchecked Return Value":
        return contract.replace(
            "payable(msg.sender).transfer(amount);",
            "msg.sender.call{value: amount}(\"\");"
        )
    elif error_type == "DoS with Gas Limit":
        return contract + "\nfunction costlyOperation() public {\n    for (uint i = 0; i < 1000000; i++) {}\n}"
    elif error_type == "Access Control Issues":
        return contract.replace(
            "function set(uint x) public {",
            "function set(uint x) public onlyOwner {"
        )
    elif error_type == "Deprecated Functions":
        return contract.replace(
            "pragma solidity ^0.8.0;",
            "pragma solidity ^0.4.0;"
        )
    elif error_type == "tx.origin Authorization":
        return contract + "\nfunction authorize() public {\n    require(tx.origin == msg.sender);\n}"
    elif error_type == "Timestamp Dependence":
        return contract.replace(
            "require(balance >= amount, \"Insufficient balance\");",
            "require(block.timestamp % 15 == 0);"
        )
    elif error_type == "Transaction Ordering Dependence":
        return contract + "\nfunction setOrder() public {\n    if (block.number % 2 == 0) {}\n}"
    elif error_type == "Selfdestruct Vulnerability":
        return contract + "\nfunction destroy() public {\n    selfdestruct(payable(msg.sender));\n}"
    else:
        return contract

# Generate 100 Solidity files with errors
for i in range(1, 101):
    base_contract = random.choice(base_contracts)
    error_type = random.choice(errors)
    modified_contract = introduce_error(base_contract, error_type)
    file_path = f"solidity_files/contract_{i}.sol"
    with open(file_path, "w") as file:
        file.write(modified_contract)

print("Generated 100 Solidity files with different errors in 'solidity_files' directory.")
