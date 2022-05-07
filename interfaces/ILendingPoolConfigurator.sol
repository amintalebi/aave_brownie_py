// SPDX-License-Identifier: agpl-3.0
pragma solidity 0.6.12;

interface ILendingPoolConfigurator {
    function setPoolPause(bool val) external;
}