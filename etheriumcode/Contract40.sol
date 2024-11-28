
    pragma solidity ^0.8.0;
    contract Deprecated {
        function useCall() public {
            address(this).call(""); // Deprecated use of call
        }
    }
    