liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

def trade(pool, pool_reserve, amount, fromm):
    alpha, beta = pool
    x, y = pool_reserve
    k = x * y
    if fromm == alpha:
        x = x + amount + amount * 0.003
        # print(x)
        receive = y - k / x
        y -= receive
    elif fromm == beta:
        y = y + amount + amount * 0.003
        # print(y)
        receive = x - k / y
        x -= receive
    liquidity.update({pool: (x, y)})

    if fromm == alpha:
        change_path.append(beta)
        return beta, receive # return to current_token and token_amount
    elif fromm == beta:
        change_path.append(alpha)
        return alpha, receive
    
def find_profitable(current_token, token_amount):
    most_profitable = 0
    most_profitable_pair = ()
    x = 0
    y = 0
    for key, value in liquidity.items():
        if current_token in key and 0 not in value:
            if current_token == key[0]:
                x = value[0]
                y = value[1]
            elif current_token == key[1]:
                x = value[1]
                y = value[0]
            k = x * y
            profit = y + k / x
            if profit > most_profitable:
                most_profitable = profit
                most_profitable_pair = key
    return most_profitable_pair
    
change_path = ["tokenB"]
current_token = "tokenB"
token_amount = 5

while token_amount < 20 or current_token != "tokenB":
    profitable_pair = find_profitable(current_token)
    # print(profitable_pair)
    current_token, token_amount = trade(profitable_pair, liquidity[profitable_pair], token_amount, current_token)

print(current_token, token_amount)
# print(change_path)
# print(current_token, token_amount)
# current_token, token_amount = trade(("tokenA", "tokenB"), liquidity[("tokenA", "tokenB")], token_amount, current_token)
# print(current_token, token_amount)
# print(liquidity[("tokenA", "tokenB")])
# print(change_path)