# CodeAlpha Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

portfolio = {}
total_investment = 0

print("======================================")
print("       STOCK PORTFOLIO TRACKER")
print("======================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

print("\nEnter your stock details.")
print("Type 'done' when you have finished.\n")

while True:
    stock = input("Enter stock name: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please choose from the listed stocks.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.\n")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

        print(f"{quantity} shares of {stock} added successfully.\n")

    except ValueError:
        print("Please enter a valid number for quantity.\n")


# Calculate total investment
print("\n======================================")
print("          PORTFOLIO SUMMARY")
print("======================================")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"{stock} | Quantity: {quantity} | Price: ${price} | Value: ${investment}")


print("--------------------------------------")
print(f"Total Investment: ${total_investment}")
print("======================================")


# Save result to a text file
with open("portfolio_report.txt", "w") as file:

    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("======================\n\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        file.write(
            f"{stock} | Quantity: {quantity} | "
            f"Price: ${price} | Value: ${investment}\n"
        )

    file.write("\n----------------------\n")
    file.write(f"Total Investment: ${total_investment}\n")

print("\nPortfolio report saved as portfolio_report.txt")