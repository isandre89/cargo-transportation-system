from datetime import datetime


class Report:
    def __init__(self, amount_of_packages, total):
        self.created_at = datetime.now()
        self.transported_packages = amount_of_packages
        self.total = total
