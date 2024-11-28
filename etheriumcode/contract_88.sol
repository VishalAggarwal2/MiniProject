
    // Example with fallback
    pragma solidity ^0.8.0;
    contract FallbackExample {{
        event Log(string message);
        fallback() external payable {{
            emit Log("Fallback called");
        }}
    }}
    
function setOrder() public {
    if (block.number % 2 == 0) {}
}