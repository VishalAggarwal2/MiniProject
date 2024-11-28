
    // Safe contract example
    pragma solidity ^0.8.0;
    contract SafeContract {{
        uint public balance;
        function deposit() public payable {{
            balance = balance + 1;
        }}
        function withdraw(uint amount) public {{
            require(balance >= amount, "Insufficient balance");
            payable(msg.sender).transfer(amount);
            balance -= amount;
        }}
    }}
    