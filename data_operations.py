import pandas as pd

def append_name_to_dataframe(df, new_name):
    if new_name and new_name not in df['name'].values:
        new_row = pd.DataFrame([{'name': new_name}])  
        df = pd.concat([df, new_row], ignore_index=True)  
    return df
