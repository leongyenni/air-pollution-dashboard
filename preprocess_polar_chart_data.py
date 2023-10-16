import pandas as pd

input_file = 'death-rate-by-risk-factor-year.csv'
df = pd.read_csv(input_file)
filtered_df = df[(df['country'] == 'Global') & (df['metric_name'] == 'Rate') & (df['death_cause'] != 'High systolic blood pressure')]
filtered_df = filtered_df.rename(
    columns={'death_cause': 'name', 'year': 'year', 'val': 'value'})
filtered_df = filtered_df.drop(columns={'country', 'metric_name'})
output_file = 'cleaned-death-rate-by-risk-factor-year.csv'
filtered_df.to_csv(output_file, index=False)
