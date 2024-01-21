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


def main():
    entries = get_entries_from_csvfile("data.csv")
    print_average_age(entries)
    print_names_by_occupation(entries)


if __name__ == "__main__":
    main()