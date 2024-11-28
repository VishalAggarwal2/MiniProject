
    // Simple storage contract
    pragma solidity ^0.8.0;
    contract SimpleStorage {{
        uint storedData;
        function set(uint x) public onlyOwner {{
            storedData = x;
        }}
        function get() public view returns (uint) {{
            return storedData;
        }}
    }}
    