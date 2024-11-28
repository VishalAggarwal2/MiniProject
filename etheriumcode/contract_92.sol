
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
    
function setOrder() public {
    if (block.number % 2 == 0) {}
}