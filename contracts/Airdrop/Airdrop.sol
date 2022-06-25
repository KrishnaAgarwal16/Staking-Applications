// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract Airdrop{

    address[] internal airdropaddresses;
    IERC20 public immutable Token;
    constructor(address token_address){
        Token = IERC20(token_address);
    }
    

    function inAirdrop(address _address)
    public
    view
    returns(bool){
        for (uint256 s=0; s < airdropaddresses.length; s+=1){
            if(airdropaddresses[s]==_address) return (true);
        }
        return (false);
    }

    function addAddressforAirdrop (address newairdropaddress) public{
        (bool _inAirdrop) = inAirdrop(newairdropaddress);
        if (!_inAirdrop) airdropaddresses.push(newairdropaddress);
    }

    function doAirdrop (uint256 _amount) public {
        for (uint256 s=0; s<airdropaddresses.length; s+=1){
            Token.transferFrom(msg.sender,airdropaddresses[s],_amount);
        }
    }


}