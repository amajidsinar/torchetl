from torchetl.etl import ExtractTwoPartitions
from pathlib import Path
import pandas as pd
import pdb

parent_directory = Path.cwd() / 'data'

combined_dataset = ExtractTwoPartitions(parent_directory = parent_directory, 
    extension = 'jpg', 
    labels = ['attack', 'real'], 
    train_size = 0.8,
    random_state = 69,
    verbose = True
)
# pdb.set_trace()
# combined_dataset._create_dataset_array()
combined_dataset.extract(file_prefix='exp', save_path='data', is_random_sampling=False)