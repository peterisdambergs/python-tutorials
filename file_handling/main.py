import csv


def main():
    entries = []

    # with open("data.csv", "r", encoding="utf-8") as f:
    #     reader = csv.DictReader(f)
    #     for row in reader:
    #         entries.append(row)

    with open("data.csv", "r", encoding="utf-8") as f:
        headers = f.readline().split(",")
        lines = f.readlines()

        for line in lines:
            line_list = line.split(",")
            name, age, country, occupation = line_list

            entry = {
                headers[0]: name,
                headers[1]: age,
                headers[2]: country,
                headers[3].strip(): occupation.strip()
            }

            entries.append(entry)

    ages = [int(entry.get("Age")) for entry in entries]
    occupations = sorted(set([entry.get("Occupation") for entry in entries]))

    for occupation in occupations:
        print(occupation, "\n--------")

        for entry in entries:
            if entry.get("Occupation") == occupation:
                print(entry.get("Name"))

        print("\n*********\n")


if __name__ == "__main__":
    main()
