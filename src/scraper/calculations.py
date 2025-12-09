def calculate_median_price(price_list: list) -> float :
    sum = 0
    for price in price_list:
        sum+=price

    return sum/len(price_list)+1