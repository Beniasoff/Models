# %%
import pandas as pd
import os
import matplotlib.pyplot as plt


# %%
def preProcess(directory_path, files_number=3,All = True):
# path = r"C:\Users\netam_8hw3bpl\OneDrive\Documents\Uni\models\finals\dryad"
    if All:
        directories = [r'Crawling\N2_adult',r'Crawling\N2_lateL1', r'Swimming\N2_adult', r'Swimming\N2_lateL1']
    else:
        directories = [r'Crawling\N2_adult',r'Swimming\N2_adult']
    fileNum = files_number

    all_data = pd.DataFrame()

    for directory in directories:
        the_path = directory_path + '\\' + directory
        files = os.listdir(the_path) 
        
        for file in files[0:fileNum]:
            data = pd.read_csv(the_path + "\\" + file, sep="\t")
            df = data.iloc[:,1:11].copy()
            if 'crawl' in file.lower() :
                df.loc[:,'movement'] = 'crawl'
            elif 'swim' in file.lower():
                df.loc[:,'movement'] = 'swim'

            if 'adult' in file.lower():
                df.loc[:,'age'] = 'adult'
            elif 'l1' in file.lower():
                df.loc[:,'age'] = 'young'
            
            all_data = pd.concat([all_data, df], ignore_index=True)

    return all_data


