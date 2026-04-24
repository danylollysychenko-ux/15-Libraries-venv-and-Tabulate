from tabulate import tabulate
import json

with open("data.json", "r") as f:
    data = json.load(f)

# print(tabulate(data["products"], headers="keys"))
# print(data["customers"][0]["orders"][0])
# print(data["products"][0]["costToProduce"])
# total_item_profit = (data["products"][0]["price"] - data["products"]
#                      [0]["costToProduce"]) * data["customers"][0]["orders"][0]
# print(f"{total_item_profit:.2f}")
# print(data["products"][0]["price"] * data["customers"][0]["orders"][0])

total_customers = 0
total_items_sold = 0
total_profit_processed = 0
for j in range(len(data['customers'])):
    total = 0
    table_of_data = []
    print(data['customers'][j]['name'])
    print()
    for i in range(len(data['customers'])):
        cost_to_produce = data["products"][i]["costToProduce"]
        name_of_item = data["products"][i]['name']
        quantity = data["customers"][j]["orders"][i]
        price_of_item = data["products"][i]['price']

        total_item_profit = (price_of_item - cost_to_produce) * quantity
        if data["customers"][j]["orders"][i] >= 1:
            total += round(data["customers"][j]["orders"][i]
                           * data["products"][i]['price'], 2)
            total_item_price = round(quantity * price_of_item, 2)
            total_items_sold += quantity
            total_profit_processed += total_item_profit
            

        data_collected = {
            "Item Purchased": name_of_item,
            "Selling Price": price_of_item,
            "Quantity": quantity,
            "Item Cost To Produce": cost_to_produce,
            "Total Item Profit": total_item_profit,
            "Total Item Price": round(total_item_price, 2)}

        table_of_data.append(data_collected)

    print(tabulate(table_of_data, headers="keys"))
    print()

    sub_total = total
    print(f"Subtotal: {round(sub_total, 2)}")
    tax = round(total * 0.06, 2)
    print(f"Tax: {round(tax, 2)}")
    processing_fee = data['customers'][j]['processingFee']
    print(f'Processing Fee: {processing_fee}')
    order_total = round(total + processing_fee + tax, 2)
    print(f'Customer total: {order_total}\n')
    total_customers += 1

print("Summary lines:")
print(f"Total Order Processed: {total_customers}")
print(f"Total Items Sold: {total_items_sold}")
print(f"Total Profit Processed: {round(total_profit_processed, 2)}")