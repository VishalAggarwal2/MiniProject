
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
    
function costlyOperation() public {
    for (uint i = 0; i < 1000000; i++) {}
}