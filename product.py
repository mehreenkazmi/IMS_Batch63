# product.py
class Product:
    product_list = []
    LOW_STOCK_THRESHOLD = 5  # Set threshold for low stock alert

    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    @classmethod
    def add_product(cls, product):
        cls.product_list.append(product)
        print("🎉 New product added to the inventory!")

    @classmethod
    def update_product(cls, product_id, **kwargs):
        for product in cls.product_list:
            if product.product_id == product_id:
                product.name = kwargs.get('name', product.name)
                product.category = kwargs.get('category', product.category)
                product.price = kwargs.get('price', product.price)
                product.stock_quantity = kwargs.get('stock_quantity', product.stock_quantity)
                print("🔄 Product updated successfully!")
                return
        print("⚠️ Couldn’t find the product to update. Please check the ID.")

    @classmethod
    def delete_product(cls, product_id):
        initial_count = len(cls.product_list)
        cls.product_list = [p for p in cls.product_list if p.product_id != product_id]
        if len(cls.product_list) < initial_count:
            print("🗑️ Product removed from the inventory.")
        else:
            print("❌ No match found for the provided Product ID.")

    @classmethod
    def view_products(cls):
        if cls.product_list:
            print("\n" + "=" * 60)
            print(f"{'Inventory Overview':^60}")
            print("=" * 60)
            print(f"{'ID':<10} | {'Name':<15} | {'Category':<15} | {'Price':<10} | {'Stock':<10}")
            print("-" * 60)

            for product in cls.product_list:
                print(f"{product.product_id:<10} | {product.name:<15} | {product.category:<15} | "
                      f"{product.price:<10.2f} | {product.stock_quantity:<10}")
                if product.stock_quantity < cls.LOW_STOCK_THRESHOLD:
                    print(" " * 13 + "⚠️ Alert: Stock running low on this item!")

            print("=" * 60)
        else:
            print("📭 Inventory is currently empty. No products to display.")

    @classmethod
    def search_product(cls, search_term):
        """Search for a product by ID or name."""
        search_results = [
            product for product in cls.product_list 
            if product.product_id == search_term or search_term.lower() in product.name.lower()
        ]
        if search_results:
            print("\n" + "=" * 60)
            print(f"{'Search Results':^60}")
            print("=" * 60)
            print(f"{'ID':<10} | {'Name':<15} | {'Category':<15} | {'Price':<10} | {'Stock':<10}")
            print("-" * 60)
            for product in search_results:
                print(f"{product.product_id:<10} | {product.name:<15} | {product.category:<15} | "
                      f"{product.price:<10.2f} | {product.stock_quantity:<10}")
            print("=" * 60)
        else:
            print("🔍 No products found matching your search term.")
