// SPDX-License-Identifier: agpl-3.0
pragma solidity 0.6.12;

interface IAaveOracle {
    function getSourceOfAsset(address asset) external view returns (address);
    function getAssetPrice(address asset) external view returns (uint256);
    function BASE_CURRENCY_UNIT() external view returns (uint256);
    function BASE_CURRENCY() external view returns (address);
}

