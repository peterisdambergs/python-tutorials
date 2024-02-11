format_headers = lambda entry: ",".join(entry.keys())
format_entry = lambda entry: f"\n{','.join(entry.values())}"


def get_entries_from_csv_file(csv_file):
    with open(csv_file, "r", encoding="utf-8") as f:
        headers = f.readline().strip().split(",")
        lines = f.readlines()

    entries = [{k: v for k, v in zip(headers, line.strip().split(","))} for line in lines]
    return entries


def print_average_age(entries):
    ages = [int(entry.get("Age")) for entry in entries]
    print(f"Average age is {round(sum(ages) / len(ages), 2)}")


def print_names_by_occupation_for_all_occupations(entries):
    occupations = sorted(set([entry.get("Occupation") for entry in entries]))
    for occupation in occupations:
        name_list = [entry.get("Name") for entry in entries if entry.get("Occupation") == occupation]
        print(f"{occupation}: {name_list}")


def add_line_to_csv_file(name, age, country, occupation):
    with open("data.csv", 'a') as f:
        f.write(f"\n{name},{age},{country},{occupation}")


def print_names_by_country(entries, country):
    names_list = [entry.get("Name") for entry in entries if entry.get("Country") == country]
    print(f"{country}: {names_list}")


def create_csv_sorted_by_age(entries):
    sorted_entries = sorted(entries, key=lambda e: e.get("Age"))

    with open("data_sorted.csv", "w") as f:
        f.write(format_headers(entries[0]))
        for entry in sorted_entries:
            f.write(format_entry(entry))


def create_csv_filtered_by_age_range(entries, min, max):
    with open(f"data_{min}_to_{max}.csv", "w") as f:
        f.write(format_headers(entries[0]))
        for entry in entries:
            if max >= int(entry.get("Age")) >= min:
                f.write(format_entry(entry))


def main():
    entries = get_entries_from_csv_file("data.csv")
    for num in range(18, 40):
        create_csv_filtered_by_age_range(entries, num, num+2)


if __name__ == "__main__":
    main()
