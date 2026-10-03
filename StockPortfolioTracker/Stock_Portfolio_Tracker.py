
import time


stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 160
}

portfolio = {}

buy_stock = True
while buy_stock:

    print("\nWhich Stock Do You Want To Buy?")
    print("AAPL - Apple")
    print("TSLA - Tesla")
    print("MSFT - Microsoft")
    print("GOOGL - Google")

    stock = input(
        "\nEnter the stock symbol (or type 'done' to finish): "
    ).strip().upper()

    if stock == "DONE":
        buy_stock = False
        continue

    if stock not in stocks:
        print("This stock doesn't exist!")
        continue

    quantity = input("Enter the quantity: ").strip()

    if not quantity.isdigit():
        print("Please enter digits only.")
        continue

    quantity = int(quantity)

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        continue

    # Add quantity to portfolio
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity


print("\n========================================")
print("          STOCK PORTFOLIO REPORT")
print("========================================")

print(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Investment'}")
print("-" * 50)

total_investment = 0

for stock, quantity in portfolio.items():

    stock_price = stocks[stock]
    investment = quantity * stock_price

    total_investment += investment

    print(
        f"{stock:<10}"
        f"{quantity:<12}"
        f"${stock_price:<11}"
        f"${investment}"
    )

print("-" * 50)
print(f"Total Investment: ${total_investment}")
print("========================================")



choice = input(
    "\nDo you want to save the report? (Yes/No): "
).strip().lower()

if choice in ["y", "yes"]:
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("Stock Portfolio Report.txt", "a") as p:
        p.write(current_time + "\n")
        p.write("========================================\n")
        p.write("          STOCK PORTFOLIO REPORT\n")
        p.write("========================================\n\n")

        p.write(
            f"{'Stock':<10}{'Quantity':<12}"
            f"{'Price':<12}{'Investment'}\n"
        )

        p.write("-" * 50 + "\n")

        for stock, quantity in portfolio.items():

            stock_price = stocks[stock]
            investment = quantity * stock_price

            p.write(
                f"{stock:<10}"
                f"{quantity:<12}"
                f"${stock_price:<11}"
                f"${investment}\n"
            )

        p.write("-" * 50 + "\n")
        p.write(f"Total Investment: ${total_investment}\n")
        p.write("========================================\n")
        p.write("\n")

    print("Report saved successfully!")