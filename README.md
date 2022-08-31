# Sales Data Analysis

Analysis of a small sales dataset with a supporting Power BI dashboard


### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Instructions](#instructions)
5. [Results](#results)
6. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

All the codes are written using Microsoft VS code. The code should run with no issues using Python versions 3.*.

## Project Motivation<a name="motivation"></a>


## Folder Structure<a name="files"></a>

- dataset
     - Data.rar
          - Data
            - Sales_April_2019.csv
            - Sales_August_2019.csv
            - Sales_December_2019.csv
            - Sales_February_2019.csv
            - Sales_January_2019.csv
            - Sales_July_2019.csv
            - Sales_June_2019.csv
            - Sales_March_2019.csv
            - Sales_May_2019.csv
            - Sales_November_2019.csv
            - Sales_October_2019.csv
            - Sales_September_2019.csv  
- combine_data.py # Script to combine the multiple files of the dataset
- clean_data.py # Script to clean the data
- Power BI dashboard.png # Power BI overview of the data
- README.md


## Instructions<a name="instructions"></a>

1. Extract the data folder(keep the data folder and the rest of the code in the same root folder)
2. Run the following commands in the project's root directory to start working on the data.

    - To run the script that combine the data files to a single csv file   
        `python combine_data.py "./Data" "combined_data.csv"`    
    The script will combine the files in the source folder "Data" and save it in a single file "combined_data.csv"
    
    - To run the script that cleans the data      
        `python clean_data.py "combined_data.csv" "cleaned_data.csv"`  
    The script will generate a new file with the cleaned "cleaned_data.csv" 


## Results<a name="results"></a>


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

