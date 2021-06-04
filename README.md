# The Moonstock API
## About + Documentation
Moonstock API offers multiple endpoints for stock data and analysis. (currently in development)

### Stock Data
**/\<TICKER\>** - Get most recently available data for a stock in the S&P500 using its ticker (where \<TICKER\> is the stock ticker, ex. /TSLA).

**/\<TICKER\>?days=\<#_OF_DAYS\>** - Get all available data from the past \<#_OF_DAYS\> (ex. the past 7 days) for a stock in the S&P500 using its ticker.

### Stock Analysis
**/EPS-indicator?=\<TICKER\>**
