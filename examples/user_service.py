class UserService:
    def fetch_users(self):
        try:
            print("Fetching users...")
            return ["User1", "User2"]

        except Exception as error:
            print(f"User Fetch Error: {error}")