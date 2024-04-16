# %%
import pandas as pd
import os


# %%
def preProcess(directory_path, files_number=3):
# path = r"C:\Users\netam_8hw3bpl\OneDrive\Documents\Uni\models\finals\dryad"

    directories = [r'Crawling\N2_adult',r'Crawling\N2_LateL1', r'Swimming\N2_adult', r'Swimming\N2_LateL1']
    fileNum = files_number

    all_data = pd.DataFrame()

    for directory in directories:
        the_path = directory_path + '\\' + directory
        files = os.listdir(the_path) 
        
        for file in files[0:fileNum]:
            data = pd.read_csv(the_path + "\\" + file, sep="\t")
            df = data.iloc[:,1:11]
            if 'crawl' in file.lower() :
                df['movement'] = 'crawl'
            elif 'swim' in file.lower():
                df['movement'] = 'swim'

            if 'adult' in file.lower():
                df['age'] = 'adult'
            elif 'l1' in file.lower():
                df['age'] = 'young'
            
            all_data = pd.concat([all_data, df], ignore_index=True)

    return all_data



