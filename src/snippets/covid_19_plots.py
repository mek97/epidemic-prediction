import pandas as pd

from epidpred.utils.directory_getters import DirectoryGetter

data_directory = DirectoryGetter.get_data_path("covid19-in-india/AgeGroupDetails.csv")
df = pd.read_csv(data_directory)

