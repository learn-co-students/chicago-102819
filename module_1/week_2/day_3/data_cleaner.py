import numpy as np
import pandas as pd




def combing_types(row):
    try:
        return row['Outcome Type'] + "\\" + row["Outcome Subtype"]
    except:
        return row['Outcome Type']
    






def clean_df(df):
    df['MonthYear'] = pd.to_datetime(df['MonthYear'])
    df['DateTime'] = pd.to_datetime(df['DateTime'])
    df['Date of Birth'] = pd.to_datetime(df['Date of Birth'])
    
    df['age_at_outcome'] = df['MonthYear'] - df['Date of Birth']
    df['days_at_outcome'] = df['age_at_outcome'].apply(lambda x: x.days)
    
    df['Name'].fillna('no_name', inplace = True)
    df['combined_outcome'] = df.apply(combing_types, axis = 1)
    df.drop(['Outcome Subtype'], axis =1, inplace = True)
    df.dropna(inplace = True)
    df.drop('MonthYear', axis = 1, inplace = True)
    
    
    return df