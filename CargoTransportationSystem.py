from datetime import datetime

from Report import Report
from constants import FIXED_SHIPPING_FEE


class CargoTransportationSystem:
    def __init__(self):
        self.packages = []
        self.total = 0

    def add_package(self, package):
        self.packages.append(package)
        self.total += FIXED_SHIPPING_FEE

    def add_packages(self, packages):
        for package in packages:
            self.packages.append(package)
            self.total += FIXED_SHIPPING_FEE

    def generate_report(self, date=datetime.now()):
        packages_for_date = [
            package
            for package in self.packages
            if package.created_at.date() == date.date()
        ]
        total_for_date = 0
        total_for_date = len(packages_for_date) * FIXED_SHIPPING_FEE
        transported_packages = len(packages_for_date)

        return Report(transported_packages, total_for_date)
