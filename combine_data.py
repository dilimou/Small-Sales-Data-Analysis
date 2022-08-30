import sys
import pandas as pd
import os


# Load the data
def load_data(folder):
    '''load data from given folder'''

    files = [file for file in os.listdir(folder)]
    
    return files


# Combine the data
def combine_data(folder,files):
    '''Merge the data to a single dataframe'''

    all_months_data = pd.DataFrame()

    for file in files:
        df = pd.read_csv(folder+"/"+file)
        all_months_data = pd.concat([all_months_data,df])

    return all_months_data


# Save the data into a single file
def save_data(all_months_data,save_path):
    '''save final data'''

    all_months_data.to_csv(save_path, index=False)  



def main():
    if len(sys.argv) == 3:

        folder, save_path = sys.argv[1:]

        print(f"Loading files from '{folder}'")
        files = load_data(folder)

        print('Combine the data...')

        all_months_data = combine_data(folder,files)
        
        print(f"Saving the data...")

        save_data(all_months_data,save_path)
        
        print(f"Data saved on a single csv file! {save_path}")
    
    else:
        print('Please provide the path to the folder containing the data and the path where the combined data will be saved '\
              'Example: python combine_data.py "./Sales_Data" "all_data.csv"')


if __name__ == '__main__':
    main()