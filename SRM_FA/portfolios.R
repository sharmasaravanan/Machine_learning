if(!require(tidyquant)) install.packages("tidyquant")
library(tidyquant) # To download the data
library(plotly) # To create interactive charts
library(timetk) # To manipulate the data series
library(dplyr)

tick <- c('AMZN', 'AAPL', 'NFLX', 'XOM', 'T')

price_data <- tq_get(tick,
                     from = '2020-01-01',
                     to = '2023-12-31',
                     get = 'stock.prices')

sample_n(price_data,4)


# Suppose we have 5 stocks (AMZN, AAPL, NFLX, XOM, T) with fictional monthly returns
set.seed(123)  # For reproducibility
monthly_returns <- matrix(rexp(20, rate = 0.1), ncol=5)
colnames(monthly_returns) <- c('AMZN', 'AAPL', 'NFLX', 'XOM', 'T')

# Computing mean returns and the covariance matrix
mean_returns <- colMeans(monthly_returns)
cov_matrix <- cov(monthly_returns)

# Imagine we're considering 1000 random portfolios
num_portfolios <- 1000
results <- matrix(nrow=num_portfolios, ncol=3)  # Store [return, risk, Sharpe Ratio]

for (i in 1:num_portfolios) {
  # Random weights assigned to stocks
  weights <- runif(5)
  weights <- weights / sum(weights)
  
  # Portfolio Return and Risk
  portfolio_return <- sum(mean_returns * weights)
  portfolio_risk <- sqrt(t(weights) %*% cov_matrix %*% weights)
  
  # Sharpe Ratio (assuming risk-free rate = 3% or 0.03)
  sharpe_ratio <- (portfolio_return - 0.03) / portfolio_risk
  
  # Storing Results
  results[i,] <- c(portfolio_return, portfolio_risk, sharpe_ratio)
}

# Finding the Optimal Portfolio (Max Sharpe Ratio)
optimal_portfolio <- results[which.max(results[,3]),]
names(optimal_portfolio) <- c("Return", "Risk", "SharpeRatio")
optimal_portfolio