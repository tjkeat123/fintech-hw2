# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> slippage in AMM is the difference between expected price and the actual price when the trade execute. Uniswap address this issue by allowing user to set a maximum slippage, where the transaction will cancel if the slippage exceeds the maximum.

def uniswap_v2_trade(amount_in, reserve_in, reserve_out, fee=0.003, max_slippage=0.05):
    amount_in_with_fee = amount_in * (1 + fee)
    k = reserve_in * reserve_out
    reserve_out_new = k / (reserve_in + amount_in_with_fee)
    expected_amount_out = reserve_out - reserve_out_new

    if expected_amount_out == 0:  # Prevent division by zero if trade is too small
        slippage = 0
    else:
        slippage = (1 - (expected_amount_out / (amount_in * reserve_out / reserve_in))) * 100

    if slippage > max_slippage:
        raise Exception("Slippage exceeds tolerance")

    return expected_amount_out, slippage 

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> to prevent zero-liquidity attacks, as the first liquidity provider could potentially withdraw a large amount of tokens with a very small deposit.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> the intention behind this is maintaining the constant product, which is the core principle behind Uniswap's AMM, where the price is determine by the relative availability of each token.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> a sandwich attack is a type of front-running attack, where the attacker places a buy order when the victim is trying to buy, which drives the price higher. then immediately sell the tokens at the new inflated price for a profit. it causes the slippage to be greater, where the token you are buying costs more then expected.