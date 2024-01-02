import random
from datetime import datetime

from Package import Package
from CargoTransportationSystem import CargoTransportationSystem
from utils import (
    validate_and_convert_date,
    validate_and_convert_location,
    validate_and_convert_integer,
    validate_and_convert_float,
    clear_console,
)


def create_demo_packages(num_packages):
    demo_packages = []

    for i in range(num_packages):
        origin = "origin" + str(i)
        destination = "destination" + str(i)
        cost = round(random.uniform(5, 150), 2)

        package = Package(
            client_id=i, origin=origin, destination=destination, cost=cost
        )
        demo_packages.append(package)

    return demo_packages


def create_normal_package():
    client_id = None
    origin = None
    destination = None
    date = None
    cost = None

    while client_id is None:
        client_id_input = input("Enter client ID: ")
        client_id = validate_and_convert_integer(client_id_input)

    while origin is None:
        origin_input = input("Enter origin: ")
        origin = validate_and_convert_location(origin_input)

    while destination is None:
        destination_input = input("Enter destination: ")
        destination = validate_and_convert_location(destination_input)

    while date is None:
        date_input = input("Enter date (DD/MM/YYYY): ")
        date = validate_and_convert_date(date_input)

    while cost is None:
        cost_input = input("Enter cost: ")
        cost = validate_and_convert_float(cost_input)

    package = Package(
        client_id=client_id,
        origin=origin,
        destination=destination,
        cost=cost,
    )
    package.created_at = date

    return package


def main():
    transportation_system = CargoTransportationSystem()

    while True:
        choice = None

        print("\nOptions:")
        print("1. Add package(s)")
        print("2. Generate report by date")
        print("3. Clear console")
        print("4. Exit")

        while choice is None:
            choice_input = input("Enter your choice: ")

            if (
                choice_input is not None
                and choice_input.isdigit()
                and int(choice_input) in (1, 2, 3, 4)
            ):
                choice = int(choice_input)

        print()

        if choice == 1:
            system_choice = int(
                input("Choose system (0 for demo, 1 for normal): ")
            )

            if system_choice == 0:
                todays_packages = None
                while todays_packages is None:
                    todays_packages_input = input(
                        "Insert amount of demo packages: "
                    )
                    todays_packages = validate_and_convert_integer(
                        todays_packages_input
                    )

                demo_packages = create_demo_packages(todays_packages)
                transportation_system.add_packages(demo_packages)
            elif system_choice == 1:
                package = create_normal_package()
                transportation_system.add_package(package)
            else:
                print(
                    "Invalid choice. Please choose 0 for demo or 1 for normal."
                )

        elif choice == 2:
            date_input = input(
                "Enter date to generate report (DD/MM/YYYY). Press 'Enter' for today: "  # noqa
            )

            if date_input == "":
                report_date = datetime.now()
            else:
                report_date = validate_and_convert_date(date_input)

            if report_date:
                report = transportation_system.generate_report(report_date)
                print(f"Report for {report_date.date()}:")
                print(
                    f"The total count of transported packages is: {report.transported_packages}"  # noqa
                )
                print(f"Total revenue is: ${report.total}")

        elif choice == 3:
            clear_console()

        elif choice == 4:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
