from utils import *

def main():
    # To create an empty dataset, provide the column names and the filepath and call create_and_save_empty_dataset
    # Supported file types: .csv
    dataset_to_create = "./data/LC_Dataset2.csv"
    dataset_columns = ["ID", "Excerpt", "SY1", "SY2", "CO1", "CO2", "LQ Code"]
    create_and_save_empty_dataset(columns=dataset_columns, filepath=dataset_to_create)

if __name__ == "__main__":
    main()
    