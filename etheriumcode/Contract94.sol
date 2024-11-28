
    pragma solidity ^0.8.0;
    contract TestContract {
        uint256 public counter; // No initialization
        function increase() {
            counter += 1; // No visibility
        }
    }
    