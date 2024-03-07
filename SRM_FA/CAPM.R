# Simulate market returns
set.seed(123) # for reproducibility
market_returns = rnorm(100, mean = 0.2, sd = 0.05) # simulate 100 random market returns

# Simulate risk-free rate
risk_free_rate = 0.03

# Assume beta for our security
beta_security = 1.2

# Calculate expected return using CAPM
expected_return = risk_free_rate + beta_security * (mean(market_returns) - risk_free_rate)
print(paste("Expected return: ", round(expected_return, 4)))