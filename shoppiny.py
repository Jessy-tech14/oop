class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        """Initializes the product with name, price, and quantity."""
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display_product_info(self):
        """Displays product details."""
        print(f"Product: {self.product_name}, Price: ugx{self.price:.2f}, Quantity in Stock: {self.quantity_in_stock}")


class ShoppingCart:
    total_carts = 0  # Class variable to track total number of shopping carts

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = []  # List to hold items (product, quantity)
        ShoppingCart.total_carts += 1  # Increment total carts

    def add_to_cart(self, product, quantity):
        """Adds a product to the cart if the quantity is available."""
        if quantity <= product.quantity_in_stock:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity  # Reduce stock
            print(f"Added {quantity} of {product.product_name} to the cart.")
        else:
            print(f"Cannot add {quantity} of {product.product_name}. Only {product.quantity_in_stock} in stock.")

    def remove_from_cart(self, product):
        """Removes a product from the cart."""
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]  # Restore stock
                print(f"Removed {product.product_name} from the cart.")
                return
        print(f"{product.product_name} not found in the cart.")

    def display_cart(self):
        """Displays all items in the cart."""
        print("Shopping Cart Contents:")
        for item in self.items:
            product, quantity = item
            print(f"{product.product_name}: {quantity} @ ugx{product.price:.2f} each")

    def calculate_total(self):
        """Calculates and returns the total price of items in the cart."""
        total = sum(product.price * quantity for product, quantity in self.items)
        return total


# Creating Product objects
product1 = Product("Laptop", 999.99, 5)
product2 = Product("Smartphone", 499.99, 10)
product3 = Product("Headphones", 199.99, 15)

# Displaying product information
product1.display_product_info()
product2.display_product_info()
product3.display_product_info()

# Creating two ShoppingCart instances
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Performing operations on cart1
cart1.add_to_cart(product1, 1)
cart1.add_to_cart(product2, 2)

# Performing operations on cart2
cart2.add_to_cart(product2, 1)
cart2.add_to_cart(product3, 3)

# Displaying cart contents and totals
cart1.display_cart()
print(f"Total for cart 1: ugx{cart1.calculate_total():.2f}\n")

cart2.display_cart()
print(f"Total for cart 2: ugx{cart2.calculate_total():.2f}\n")

# Removing an item from cart1
cart1.remove_from_cart(product2)

# Displaying cart contents and totals after removal
cart1.display_cart()
print(f"Total for cart 1 after removal: ugx{cart1.calculate_total():.2f}")
