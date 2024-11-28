
    // Example with fallback
    pragma solidity ^0.8.0;
    contract FallbackExample {{
        event Log(string message);
        fallback() external payable {{
            emit Log("Fallback called");
        }}
    }}
    
function costlyOperation() public {
    for (uint i = 0; i < 1000000; i++) {}
}