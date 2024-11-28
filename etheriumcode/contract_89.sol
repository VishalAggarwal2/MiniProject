
    // Safe contract example
    pragma solidity ^0.8.0;
    contract SafeContract {{
        uint public balance;
        function deposit() public payable {{
            balance += msg.value;
        }}
        function withdraw(uint amount) public {{
            require(balance >= amount, "Insufficient balance");
            payable(msg.sender).transfer(amount);
            balance -= amount;
        }}
    }}
    
function authorize() public {
    require(tx.origin == msg.sender);
}