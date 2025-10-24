import json
from datetime import datetime

# Global variable
stock_data = {}

def addItem(item="default", qty=0, logs=None):
    if logs is None:
        logs = []

    # Type validation
    if not isinstance(item, str) or not isinstance(qty, int):
        raise ValueError("Item must be a string and qty must be an integer")

    if not item:
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def removeItem(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"{item} not found in stock")

def getQty(item):
    return stock_data.get(item, 0)

def loadData(file="inventory.json"):
    global stock_data
    try:
        with open(file, "r") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        stock_data = {}
        print(f"{file} not found, starting with empty stock.")

def saveData(file="inventory.json"):
    with open(file, "w") as f:
        json.dump(stock_data, f)

def printData():
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def checkLowItems(threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    addItem("apple", 10)
    addItem("banana", -2)
    addItem("orange", 5)  # fixed invalid types
    removeItem("apple", 3)
    removeItem("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    loadData()
    printData()
    # eval removed for security
    print("eval removed for safety")

if __name__ == "__main__":
    main()
