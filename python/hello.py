def exchange_money(money):
    # 硬币面额
    coins = [5, 2, 1]
    # 统计每个面额需要的硬币数量
    counts = [0, 0, 0]

    # 按照面额从大到小遍历硬币
    for i, coin in enumerate(coins):
        # 如果当前面额大于等于要兑换的金额
        if coin <= money:
            # 计算需要的硬币数量
            count = money // coin
            # 更新剩余金额
            money = money % coin
            # 更新硬币数量统计
            counts[i] = count

    # 输出兑换结果
    print(f"将{money}元兑换成硬币的方案：")
    for coin, count in zip(coins, counts):
        print(f"{coin}分硬币：{count}个")


# 测试兑换10元
exchange_money(1000)
