import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from tqdm import tqdm

new_df = pd.read_csv('/new_analysis.csv')

new_df = new_df.drop(columns=['filename'])

new_df['waveform_data'] = new_df['waveform_data'].apply(eval)

min_max_scaler = MinMaxScaler()
waveform_data_min_max = new_df['waveform_data'].apply(lambda x: list(min_max_scaler.fit_transform(np.array(x).reshape(-1, 1)).flatten()))

standard_scaler = StandardScaler()
waveform_data_z_norm = new_df['waveform_data'].apply(lambda x: list(standard_scaler.fit_transform(np.array(x).reshape(-1, 1)).flatten()))

other_columns = new_df.drop(columns=['waveform_data'])

min_max_scaler = MinMaxScaler()
other_columns_min_max = pd.DataFrame(min_max_scaler.fit_transform(other_columns), columns=other_columns.columns)

standard_scaler = StandardScaler()
other_columns_z_norm = pd.DataFrame(standard_scaler.fit_transform(other_columns), columns=other_columns.columns)

min_max_normalized_df = other_columns_min_max.copy()
min_max_normalized_df['waveform_data'] = waveform_data_min_max

z_norm_normalized_df = other_columns_z_norm.copy()
z_norm_normalized_df['waveform_data'] = waveform_data_z_norm

min_max_normalized_df.to_csv('min_max_normalized.csv', index=False)
z_norm_normalized_df.to_csv('z_norm_normalized.csv', index=False)
