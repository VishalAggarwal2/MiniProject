
    // Safe contract example
    pragma solidity ^0.8.0;
    contract SafeContract {{
        uint public balance;
        function deposit() public payable {{
            balance += msg.value;
        }}
        function withdraw(uint amount) public {{
            require(block.timestamp % 15 == 0);
            payable(msg.sender).transfer(amount);
            balance -= amount;
        }}
    }}
    