class OrderService:
    def fetch_orders(self):
        try:
            print("Fetching orders...")
            return ["Order1", "Order2"]

        except Exception as error:
            print(f"Order Fetch Error: {error}")