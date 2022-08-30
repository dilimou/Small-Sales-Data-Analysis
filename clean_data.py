import sys
import pandas as pd



def clean_data(file):
    ''' clean and return dataframe'''


    all_data = pd.read_csv(file)

    print(all_data.head())
    print(all_data.info())
    print(all_data.describe())

    # Check for null values
    print(f"Sum of null values in the file: {all_data.isna().sum().sum()}") # Null values accross all the data set

    print(f"Sum of null values per column: {all_data.isna().sum()}") # Null values for each column

    print("Dropping the rows with null values...")

    new_data = all_data.dropna(axis=0, how='all').copy(deep=True)


    # Remove rows witn incorrect data

    print("Dropping rows with incorrect data types...")
    new_new_data = new_data[new_data['Quantity Ordered'] != "Quantity Ordered"].copy(deep=True)

    print("Converting 'Price Each' column data type to numerical")
    new_new_data['Price Each'] = pd.to_numeric(new_new_data['Price Each'])

    print("Converting 'Order Date' column to date time")
    new_new_data['Order Date'] = pd.to_datetime(new_new_data['Order Date'])

    print("Converting 'Quantity Ordered' column to date time")
    new_new_data['Quantity Ordered'] = pd.to_numeric(new_new_data['Quantity Ordered'])

    print("Current data Info")
    new_new_data.info()


    #add city column
    print("Adding 'City' column...")
    new_new_data['City'] = new_new_data['Purchase Address'].apply(lambda x: x.split(',')[1].strip()+"("+x.split(',')[2].split(' ')[1]+")")

    #add total price column
    print("Adding 'Total Price' column...")
    new_new_data['Total Price'] = new_new_data.loc[:,'Quantity Ordered']*new_new_data.loc[:,'Price Each']

    #add month column
    print("Adding 'Month' column...")
    new_new_data['Month']=new_new_data.loc[:,'Order Date'].dt.month

    #add day column
    print("Adding 'Day' column...")
    new_new_data['Day']=new_new_data.loc[:,'Order Date'].dt.day

    return new_new_data



def save_data(new_new_data,save_path):
    '''save final data'''
    
    # export to a csv file

    new_new_data.to_csv(save_path, index=False)      


def main():
    if len(sys.argv) == 3:

        file, save_path = sys.argv[1:]


        print('Cleaning the data...')
        df = clean_data(file)
        
        print(f"Saving data to {save_path}...")
        save_data(df, save_path)
        
        print('Cleaned data saved to new file!')
    
    else:
        print('Please provide the path to the csv file and the path to save the cleaned data '\
              'Example: python combine_data.py "./Sales_Data" "all_data.csv"')


if __name__ == '__main__':
    main()