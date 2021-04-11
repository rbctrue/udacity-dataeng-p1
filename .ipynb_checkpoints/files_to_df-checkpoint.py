import numpy as np
import pandas as pd
import os
import glob
import openpyxl

# Return all json files from entered file path

def get_files(filepath, extensiontype):
    '''Retrieves the names of all files of selected file type in inputed filepath

    INPUT:
    filepath: string providing folder/repository files are located in
    fileextension: select extension type you want to retrieve - json, csv, or xlsx
    do not include period "." infront of extension name
    
    OUTPUT:
    Outputs list of file names
    '''
    
    all_files = []
    print(os.walk(filepath))
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.' + extensiontype))
        for f in files :
            print(os.path.abspath(f))
            all_files.append(os.path.abspath(f))
    
    return all_files


# create function to fill a dataframe
def files_to_df(data, extensiontype):
    '''Convert an list or dict of json files into a df
    
    INPUT:
    data: data should be a list, dictionary, or series of 
    json file names with path to be accessed
    
    OUTPUT:
    dataframe containing json content
    ''' 
    # Create a blank data frame
    df = pd.DataFrame()
    
    # Transform extension entry to all uppercase
    extensiontype = extensiontype.upper()
    
    # Loop through song files and fill df
    try:
        if extensiontype == 'JSON':
            df_new_file = pd.read_json(data, lines=True)
            df = df.append(df_new_file, ignore_index=True) 
        elif extensiontype == 'CSV':
            df_new_file = pd.read_csv(data)
            df = df.append(df_new_file, ignore_index=True)       
        else:
            print('please select either json or csv for extension')
            exit()
    except Exception as e:
        print(' Something went wrong, \
                \n check that your list has \
                \n correct file paths and only \
                \n includes json files.')
        print('Exception raised: {}'.format(e))
    
    return df

def df_main(filepath, extension):
    '''
    - Adds the names of all file types with selected extension (json or csv) into a list

    - Reads all files in list into a data frame
    '''
    #file_list = get_files(filepath, extension)
    df = files_to_df(filepath, extension)

    return df


if __name__ == "__main__":
   print('this file is meant to be called in other files')