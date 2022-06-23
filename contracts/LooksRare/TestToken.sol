// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";

import {ITestToken} from "./ITestToken.sol";

contract TestToken is ERC20, Ownable, ITestToken {
    uint256 private immutable _SUPPLY_CAP;

    constructor(
        address _premintReceiver,
        uint256 _premintAmount,
        uint256 _cap
    ) ERC20("Test Token", "TEST") {
        require(_cap >= _premintAmount, "TEST: Premint amount is greater than cap");
        // Transfer the sum of the premint to address
        _mint(_premintReceiver, _premintAmount);
        _SUPPLY_CAP = _cap;
    }

    
    function mint(address account, uint256 amount) external override onlyOwner returns (bool status) {
        if (totalSupply() + amount <= _SUPPLY_CAP) {
            _mint(account, amount);
            return true;
        }
        return false;
    }

    function SUPPLY_CAP() external view override returns (uint256) {
        return _SUPPLY_CAP;
    }
}