from datetime import datetime

from constants import FIXED_SHIPPING_FEE


class Package:
    def __init__(self, client_id, origin, destination, cost):
        self.created_at = datetime.now()
        self.client_id = client_id
        self.origin = origin
        self.destination = destination
        self.cost = cost
        self.shipping_fee = FIXED_SHIPPING_FEE
