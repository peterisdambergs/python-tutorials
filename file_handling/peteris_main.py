def get_entries_from_csvfile(csvfile):
    with open(csvfile, "r") as f:
        headers = f.readline().strip().split(",")
        lines = f.readlines()

        entries = []
        for line in lines:
            line = line.strip().split(",")
            entry = {headers[0]: line[0], headers[1]: line[1], headers[2]: line[2], headers[3]: line[3]}
            entries.append(entry)
        return entries


def main():
    entries = get_entries_from_csvfile("data.csv")
    


if __name__ == "__main__":
    main()
