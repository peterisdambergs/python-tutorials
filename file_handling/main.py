def get_headers_and_lines_from_csv_file(csv_file):
    with open(csv_file, "r", encoding="utf-8") as f:
        headers = f.readline().strip().split(",")
        lines = f.readlines()

    return headers, lines


def get_entry_from_line(line, headers):
    line_list = line.strip().split(",")

    entry = {}
    for key, value in zip(headers, line_list):
        entry[key] = value

    return entry


def get_entries_from_csv(csv_file):
    headers, lines = get_headers_and_lines_from_csv_file(csv_file)
    entries = []

    for line in lines:
        entry = get_entry_from_line(line, headers)
        entries.append(entry)

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
    entries = get_entries_from_csv("data.csv")
    print_average_age(entries)
    print_names_by_occupation(entries)


if __name__ == "__main__":
    main()
