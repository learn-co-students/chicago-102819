import pandas as pd
import numpy as np

def outcome_combiner(row):
    try: 
        if np.isnan(row['Outcome Subtype']):
            return row['Outcome Type']
    except:
        return row['Outcome Type'] + '/' + row['Outcome Subtype']


def male_or_female(sex):
    """
    Consolidate sexes into male, female, or unknown
    """
    if ' male' in sex.lower():
        return 'male'
    elif 'female' in sex.lower():
        return 'female'
    else:
        return 'Unknown'

    
    
def clean_data(df):
    df.drop_duplicates(['Animal ID'], inplace = True)
    
    df.Name.fillna('no_name', inplace = True)
    
    #Create outcome types which combine primary and secondary outcomes
    df['combined_outcome'] = df.apply(outcome_combiner, axis = 1)
    df.drop(['Outcome Type', 'Outcome Subtype'], axis = 1, inplace = True)
    
    df['MonthYear'] = pd.to_datetime(df['MonthYear'])
    df.drop('Date of Birth', axis = 1, inplace = True)
    
    df.dropna(subset = ['Sex upon Outcome'], inplace = True)
    df['sex'] = df['Sex upon Outcome'].map(male_or_female)
    df.drop('Sex upon Outcome', axis = 1, inplace = True)
    df.dropna(inplace = True)
    
    return df
