
    // Example with fallback
    pragma solidity ^0.4.0;
    contract FallbackExample {{
        event Log(string message);
        fallback() external payable {{
            emit Log("Fallback called");
        }}
    }}
    