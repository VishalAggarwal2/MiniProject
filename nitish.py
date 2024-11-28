import random
import string
import secrets
from manticore.ethereum import ManticoreEVM

# Function to generate a random string of fixed length
def random_string(length=8):
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))

# Function to generate random smart contract in Solidity
def generate_random_smart_contract():
    # Random contract name
    contract_name = random_string(10)
    
    # Random state variables and types
    state_variables = ['uint256', 'address', 'bool', 'string']
    num_variables = random.randint(1, 5)
    variables = [f"{random.choice(state_variables)} {random_string(5)};" for _ in range(num_variables)]
    
    # Random function
    function_types = ['public', 'private', 'internal']
    function_signatures = [
        'function setValue(uint256 _value) public',
        'function getValue() public view returns (uint256)',
        'function setAddress(address _addr) public',
        'function toggleActive() public'
    ]
    
    num_functions = random.randint(1, 3)
    functions = [random.choice(function_signatures) for _ in range(num_functions)]
    
    # Generating the contract template with variables and functions
    contract_template = f"""
    pragma solidity ^0.8.0;

    contract {contract_name} {{
        {' '.join(variables)}

        {f'\n'.join(functions)}
    }}
    """
    return contract_template

# Function to run Manticore on the generated contract
def check_contract_with_manticore(contract_code):
    m = ManticoreEVM()
    
    # Deploy the contract
    contract = m.create_contract(contract_code)
    
    # Start symbolic execution
    m.run()

# Main function
def main():
    # Generate a random smart contract
    contract_code = generate_random_smart_contract()
    
    print("Generated Smart Contract:")
    print(contract_code)
    
    # Check the contract with Manticore
    check_contract_with_manticore(contract_code)

if __name__ == '__main__':
    main()
