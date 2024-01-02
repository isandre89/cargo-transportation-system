from datetime import datetime


class Client:
    def __init__(self, client_id, fullname, country):
        self.client_id = client_id
        self.fullname = fullname
        self.country = country
        self.created_at = datetime.now()

    def __str__(self):
        return (
            f"Client ID: {self.client_id}\n"
            f"Full name: {self.fullname}\n"
            f"Country: {self.country}\n"
            f"Created at: {self.created_at}\n"
        )
