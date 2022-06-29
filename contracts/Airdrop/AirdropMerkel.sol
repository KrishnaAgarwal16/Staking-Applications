// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";
import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract AirdropMerkel{
    IERC20 public immutable Token;
    bytes32 public immutable root;
    mapping(address => bool) claimed;
    constructor(address token_address, bytes32 _root){
        Token = IERC20(token_address);
        root = _root;
    }
    
    function doAirdrop (bytes32[] calldata _proof, uint256 _amount) public {
        require(!claimed[msg.sender], "Already claimed air drop");
        claimed[msg.sender] = true;
        bytes32 _leaf = keccak256(abi.encodePacked(msg.sender));
        require(
            MerkleProof.verify(_proof, root, _leaf),
            "Incorrect merkle proof"
        );
        
        Token.transfer(msg.sender,_amount*10**18);
    }
}
