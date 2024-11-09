class Product:
    product_list = []
    LOW_STOCK_THRESHOLD = 5  # Define a low stock threshold for warnings

    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    @classmethod
    def add_product(cls, product):
        cls.product_list.append(product)
        print("✅ Product added successfully.")

    @classmethod
    def update_product(cls, product_id, **kwargs):
        for product in cls.product_list:
            if product.product_id == product_id:
                product.name = kwargs.get('name', product.name)
                product.category = kwargs.get('category', product.category)
                product.price = kwargs.get('price', product.price)
                product.stock_quantity = kwargs.get('stock_quantity', product.stock_quantity)
                print("✅ Product updated successfully.")
                return
        print("❌ Product not found.")

    @classmethod
    def delete_product(cls, product_id):
        initial_count = len(cls.product_list)
        cls.product_list = [p for p in cls.product_list if p.product_id != product_id]
        if len(cls.product_list) < initial_count:
            print("✅ Product deleted successfully.")
        else:
            print("❌ Product not found.")

    @classmethod
    def view_products(cls):
        if cls.product_list:
            # Print table header
            print("\n" + "=" * 60)
            print(f"{'Product Inventory':^60}")
            print("=" * 60)
            print(f"{'ID':<10} | {'Name':<15} | {'Category':<15} | {'Price':<10} | {'Stock':<10}")
            print("-" * 60)

            # Print each product in the table row by row
            for product in cls.product_list:
                print(f"{product.product_id:<10} | {product.name:<15} | {product.category:<15} | "
                      f"{product.price:<10.2f} | {product.stock_quantity:<10}")

                # Low stock warning
                if product.stock_quantity < cls.LOW_STOCK_THRESHOLD:
                    print(" " * 13 + "⚠️  Low Stock Warning: Consider restocking this item.")

            print("=" * 60)
        else:
            print("⚠️  No products in the inventory.")
