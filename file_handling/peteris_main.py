def get_entries_from_csvfile(csvfile):
    with open(csvfile, "r") as f:
        headers = f.readline().strip().split(",")
        lines = f.readlines()

        entries = []
        for line in lines:
            line = line.strip().split(",")
            entry = {headers[0]: line[0], headers[1]: int(line[1]), headers[2]: line[2], headers[3]: line[3]}
            entries.append(entry)
        return entries


def print_average_age(entries):
    ages = [entry.get("Age") for entry in entries]
    print(f"Average age: {sum(ages) / len(ages)}")


def print_names_by_occupation(entries):
    occupations = sorted(set([entry.get("Occupation") for entry in entries]))
    for occupation in occupations:
        names = [entry.get("Name") for entry in entries if occupation == entry.get("Occupation")]
        print(occupation, names)


def add_new_entry_to_csvfile(name, age, country, occupation):
    with open("data.csv", "a") as f:
        f.write(f"\n{name},{age},{country},{occupation}")


def print_names_by_country(entries, country):
    names = [entry.get("Name") for entry in entries if entry.get("Country") == country]
    print(f"{country} => {names}")


def update_csvfile_age_by_name(csvfile, name, age):
    entries = get_entries_from_csvfile(csvfile)
    with open(csvfile, "w") as f:
        f.write(','.join(entries[0].keys()))
        for entry in entries:
            entry["Age"] = str(age) if entry.get("Name") == name else str(entry.get("Age"))
            f.write(f"\n{','.join(entry.values())}")


def main():
    entries = get_entries_from_csvfile("data.csv")
    # print_average_age(entries)
    # print_names_by_occupation(entries)
    # print_names_by_country(entries, "Germany")
    update_csvfile_age_by_name("data.csv", "Erik", 25)


if __name__ == "__main__":
    main()
