# find the maximum profit after selling the stock at right time
# ex- INPUT--[7,1,5,3,6,4] OUTPUT--5(the maximum profit

def max_profit(stocks):
    array = []
    maximum = stocks[len(stocks) - 1]

    for i in range(len(stocks) - 1, -1,
                   -1):  # since the stocks are need to sale after buying so we are calculating the maximum stock from the end

        if (stocks[i] > maximum):
            maximum = stocks[i]
        array.append(maximum)

    profit = 0  # finding the maximum profit

    for i in range(len(stocks)):
        hold = array[len(stocks) - i - 1] - stocks[i]
        if (hold > profit):
            profit = hold

    return (profit)


stocks = [7, 2, 1, 1, 1, 1]
print(max_profit(stocks))