import unittest
from datetime import datetime, timedelta

from Package import Package
from CargoTransportationSystem import CargoTransportationSystem
from constants import FIXED_SHIPPING_FEE
from utils import get_random_cost


class TestPackage(unittest.TestCase):
    def test_cost_and_shipping_fee(self):
        package = Package(1, "Brasil", "Singapore", 28.43)

        self.assertEqual(package.shipping_fee, FIXED_SHIPPING_FEE)
        self.assertEqual(package.cost, 28.43)


class TestCargoTransportationSystem(unittest.TestCase):
    def test_add_package(self):
        package = Package(
            1, "United Arab Emirates", "United Kingdom", cost=96.23
        )
        transportation_system = CargoTransportationSystem()
        transportation_system.add_package(package)

        self.assertEqual(len(transportation_system.packages), 1)
        self.assertEqual(transportation_system.total, FIXED_SHIPPING_FEE)

    def test_add_packages(self):
        packages = []
        amount_of_packages = 16

        for i in range(amount_of_packages):
            origin = "origin" + str(i)
            destination = "destination" + str(i)

            package = Package(
                client_id=i,
                origin=origin,
                destination=destination,
                cost=get_random_cost(),
            )

            packages.append(package)

        transportation_system = CargoTransportationSystem()
        transportation_system.add_packages(packages)

        self.assertEqual(
            len(transportation_system.packages), amount_of_packages
        )
        self.assertEqual(
            transportation_system.total,
            FIXED_SHIPPING_FEE * amount_of_packages,  # noqa
        )

    def test_generate_report_for_today(self):
        transportation_system = CargoTransportationSystem()

        amount_of_packages = 5

        for i in range(amount_of_packages):
            cost = get_random_cost()
            origin = "origin" + str(i)
            destination = "destination" + str(i)

            package = Package(
                client_id=i, origin=origin, destination=destination, cost=cost
            )
            transportation_system.add_package(package)

        today = datetime.now()
        report = transportation_system.generate_report(date=today)

        self.assertEqual(report.transported_packages, amount_of_packages)
        self.assertEqual(report.total, amount_of_packages * FIXED_SHIPPING_FEE)

    def test_generate_report_for_yesterday(self):
        transportation_system = CargoTransportationSystem()

        amount_of_packages = 5

        for i in range(amount_of_packages):
            cost = get_random_cost()
            origin = "origin" + str(i)
            destination = "destination" + str(i)

            package = Package(
                client_id=i, origin=origin, destination=destination, cost=cost
            )

            if i == 2:
                package.created_at = datetime.now() - timedelta(days=1)

            transportation_system.add_package(package)

        yesterday = datetime.now() - timedelta(days=1)
        report = transportation_system.generate_report(date=yesterday)

        self.assertEqual(report.transported_packages, 1)
        self.assertEqual(report.total, FIXED_SHIPPING_FEE)


if __name__ == "__main__":
    unittest.main(verbosity=2)
