class ProductService:
    def fetch_products(self):
        try:
            print("Fetching products...")
            return ["Product1", "Product2"]

        except Exception as error:
            print(f"Product Fetch Error: {error}")