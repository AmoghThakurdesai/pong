import pandas as pd

FILE_PATH = "/media/amogh193/Data/PythonFiles/assignment/fullstackapp/seaborn-data-master/dataset_names.txt"
SEABORN_FILE_PATH = "/media/amogh193/Data/PythonFiles/assignment/fullstackapp/seaborn-data-master"

def selecttable(selected):
    f = open(FILE_PATH,'r')
    datasetnames = f.read().split()
    tableheading = datasetnames[selected] if selected < 22 else datasetnames[0]
    f.close()
    df = pd.read_csv(f"{SEABORN_FILE_PATH}/csv/{tableheading}.csv")
    table = df.to_html()
    return table,tableheading,datasetnames
  