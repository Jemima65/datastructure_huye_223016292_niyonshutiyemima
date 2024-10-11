class GroceryStore:
    def __init__(self):
        self.inventory = []  # List to store inventory items
        self.queue = []      # List to manage customer queue
        self.cancellations = []  # Stack for cancellations

    def add_item(self, item_id, item_name, price, stock):
        """Add a new item to the inventory."""
        self.inventory.append({
            'ItemID': item_id,
            'ItemName': item_name,
            'Price': price,
            'Stock': stock
        })

    def show_inventory(self):
        """Display current inventory."""
        print("\nCurrent Inventory:")
        for item in self.inventory:
            print(f"{item['ItemID']}: {item['ItemName']} - ${item['Price']} (Stock: {item['Stock']})")

    def add_to_queue(self):
        """Add a customer to the queue with selected items from user input."""
        customer_name = input("Enter the customer's name: ")
        print("Available items to purchase:")
        for item in self.inventory:
            print(f"{item['ItemID']}: {item['ItemName']} - ${item['Price']} (Stock: {item['Stock']})")

        item_ids = input("Enter the Item IDs separated by commas: ")
        item_ids = [int(i.strip()) for i in item_ids.split(",")]

        total_amount = 0
        valid_purchase = True

        for item_id in item_ids:
            for item in self.inventory:
                if item['ItemID'] == item_id:
                    if item['Stock'] > 0:
                        total_amount += item['Price']
                        item['Stock'] -= 1  # Decrease stock by 1
                    else:
                        print(f"Sorry, {item['ItemName']} is out of stock.")
                        valid_purchase = False
                    break

        if valid_purchase:
            self.queue.append({
                'CustomerName': customer_name,
                'ItemsPurchased': item_ids,
                'TotalAmount': total_amount
            })
            print(f"{customer_name} has been added to the queue with total amount: ${total_amount:.2f}.")
            self.show_queue()  # Show queue after action
        else:
            print(f"{customer_name} could not be added to the queue due to stock issues.")

    def show_queue(self):
        """Display current queue of customers."""
        print("\nCurrent Queue:")
        if not self.queue:
            print("No customers in the queue.")
        else:
            for customer in self.queue:
                print(f"Customer: {customer['CustomerName']}, Total Amount: ${customer['TotalAmount']:.2f}")

    def process_customers(self):
        """Loop to allow continuous customer operations including add customer and showing queue and inventory."""
        while True:
            action = input("\nChoose an action: \n(1) Add Customer \n(2) Show Queue \n(3) Show Inventory \n(4) Exit \nchoose the option to perform:").strip()
            
            if action == '1':
                self.add_to_queue()
            elif action == '2':
                self.show_queue()
            elif action == '3':
                self.show_inventory()
            elif action == '4':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

# Example Usage
store = GroceryStore()

# Adding items to the inventory
items = [
    (401, 'Milk', 2.50, 10),
    (402, 'Bread', 1.20, 15),
    (403, 'Eggs', 3.00, 20),
    (404, 'Butter', 2.75, 25),
    (405, 'Cheese', 4.50, 30),
    (406, 'Apples', 1.50, 50),
    (407, 'Bananas', 1.20, 40),
    (408, 'Oranges', 1.80, 35),
    (409, 'Grapes', 2.00, 45),
    (410, 'Chicken Breast', 5.00, 15),
    (411, 'Beef Steak', 7.50, 10),
    (412, 'Salmon', 8.00, 12),
    (413, 'Rice', 1.00, 100),
    (414, 'Pasta', 1.20, 80),
    (415, 'Tomato Sauce', 1.50, 60),
    (416, 'Cereal', 3.20, 25),
    (417, 'Yogurt', 2.00, 30),
    (418, 'Orange Juice', 3.00, 20),
    (419, 'Coffee', 5.00, 15),
    (420, 'Tea', 4.00, 20),
    (421, 'Sugar', 1.50, 50),
    (422, 'Flour', 1.80, 40)
]

for item in items:
    store.add_item(*item)

store.process_customers()
