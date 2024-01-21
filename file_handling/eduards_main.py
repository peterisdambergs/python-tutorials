def get_entries_from_csv_file(csv_file):
    with open(csv_file, "r", encoding="utf-8") as f:
        headers = f.readline().strip().split(",")
        lines = f.readlines()

    entries = [{k: v for k, v in zip(headers, line.strip().split(","))} for line in lines]
    return entries


def print_average_age(entries):
    ages = [int(entry.get("Age")) for entry in entries]
    print(f"Average age is {sum(ages)/len(ages)}")


def print_names_by_occupation(entries):
    occupations = sorted(set([entry.get("Occupation") for entry in entries]))
    for occupation in occupations:
        name_list = [entry.get("Name") for entry in entries if entry.get("Occupation") == occupation]
        print(f"{occupation}: {name_list}")


def main():
    entries = get_entries_from_csv_file("data.csv")
    print_average_age(entries)
    print_names_by_occupation(entries)


if __name__ == "__main__":
    main()
