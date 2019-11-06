import numpy as np
import pandas as pd




def combing_types(row):
    try:
        return row['Outcome Type'] + "\\" + row["Outcome Subtype"]
    except:
        return row['Outcome Type']
    






def clean_df(df):
    
    df['Name'].fillna('no_name', inplace = True)
    df['combined_outcome'] = df.apply(combing_types, axis = 1)
    df.drop(['Outcome Subtype'], axis =1, inplace = True)
    df.dropna(inplace = True)
    
    
    return df