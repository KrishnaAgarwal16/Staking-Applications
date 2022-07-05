// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ERC4973.sol";

contract SoulBound is ERC4973 {
    address public owner;
    uint256 public count = 0;

    constructor () ERC4973("Soul", "SL") {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    function burn(uint256 _tokenId) external override {
        require(ownerOf(_tokenId) == msg.sender || msg.sender == owner, "You can't revoke this token");
        _burn(_tokenId);
    }

    function issue(address _issuee, string calldata _uri) external onlyOwner {
        _mint(_issuee, count, _uri);
        count += 1;
    }

    
}