import pandas as pd

def load_data(filename):
    """
    FUNCTION load_data(filename):
    data ← empty dictionary

    OPEN filename as CSV file:
        FOR each row in CSV:
            name   ← row["name"]
            mother ← row["mother"]  OR None if blank
            father ← row["father"]  OR None if blank
            trait  ← True  if row["trait"] == "1"
                     False if row["trait"] == "0"
                     None  otherwise (unknown)

            data[name] ← { name, mother, father, trait }

    RETURN data
    """
    data={}
    file=pd.read_csv(filename)
    for _, row in file.iterrows():
        name=row["name"]
        mother=row["mother"]
        father=row["father"]
        trait=None
        if row["trait"]=="0":
            trait=False
        if row["trait"]=="1": 
            trait=True
        else: 
            trait=None
            
        data[name]={name, mother,father,trait}
    return data