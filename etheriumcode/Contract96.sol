
    pragma solidity ^0.8.0;
    contract EtherTransfer {
        function sendEther(address payable recipient) public {
            recipient.transfer(address(this).balance); // Unrestricted transfer
        }
    }
    