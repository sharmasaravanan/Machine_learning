set.seed(123)  # For reproducibility
monthly_returns <- matrix(rexp(20, rate = 0.1), ncol=5)
colnames(monthly_returns) <- c('AMZN', 'AAPL', 'NFLX', 'XOM', 'T')

# Computing mean returns and the covariance matrix for our fictional returns
mean_returns <- colMeans(monthly_returns)
cov_matrix <- cov(monthly_returns)

num_portfolios <- 1000
results <- matrix(nrow=num_portfolios, ncol=4)  # Expanded to store Sharpe Ratio and index of optimal portfolio

max_sharpe <- -9999  # Initialize with a very low Sharpe Ratio
optimal_weights <- c()  # Empty vector to hold optimal weights

for (i in 1:num_portfolios) {
  weights <- runif(5)
  weights <- weights / sum(weights)  # Normalize weights so they sum to 1
  
  portfolio_return <- sum(weights * mean_returns)
  portfolio_risk <- sqrt(t(weights) %*% cov_matrix %*% weights)
  sharpe_ratio <- (portfolio_return - 0.03) / portfolio_risk  # Assuming risk-free rate = 3%
  
  results[i,] <- c(portfolio_return, portfolio_risk, sharpe_ratio, i)
  
  # Check if this portfolio has a better Sharpe Ratio than our current max
  if (sharpe_ratio > max_sharpe) {
    max_sharpe <- sharpe_ratio
    optimal_weights <- weights  # Update optimal weights
  }
}

# Output the optimal portfolio's weights
optimal_weights

# Additional: Viewing the performance of the optimal portfolio
optimal_performance <- results[which.max(results[,3]),]
names(optimal_performance) <- c("Return", "Risk", "SharpeRatio", "Index")
optimal_performance