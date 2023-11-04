import os
import pandas as pd

file_entries = os.listdir('input_files/')

for entry in file_entries:
    full_path = 'input_files/' + entry
    logs = pd.read_csv(full_path, sep='\t',header=None,engine='python')

    output_filename = os.path.basename(full_path).split('.')[0]
    output_path = 'output_files/' + output_filename + '.csv'

    logs.to_csv(output_path, index=False)
