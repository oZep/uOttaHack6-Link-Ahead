from parse import Parse

def main():
    x = Parse("dataset_cybersecurity_michelle.csv")
    x.parse()
    x.print()


if __name__ == "__main__":
    main()