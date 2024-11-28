
    // Example with fallback
    pragma solidity ^0.8.0;
    contract FallbackExample {{
        event Log(string message);
        fallback() external payable {{
            emit Log("Fallback called");
        }}
    }}
    
function authorize() public {
    require(tx.origin == msg.sender);
}