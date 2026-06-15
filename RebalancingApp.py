def calculate_shares(portfolio_value, target_pct, current_pct, price):
    target_value = portfolio_value * (target_pct / 100)
    current_value = portfolio_value * (current_pct / 100)
    dollar_diff = target_value - current_value
    shares = dollar_diff / price
    return round(shares, 2)