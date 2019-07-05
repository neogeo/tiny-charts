## A program to display tiny stockcharts

This will open a browser and dispaly tiny charts for any number of stock tickers. It supports the command line or csv's exported from ThinkOrSwim's Scan results. 

## Setup
```
    python3.6 -m venv .env
    . .env/bin/activate
```

## Run
### Command-line
Provide a space separated list of symbols
```
python open_stock_charts [-s] [list-of-symbols]
```
### CSV File

Provide a CSV named 'results.csv' (with one column "results"). See example `results.csv`:
```
    python open_stock_charts 
'''