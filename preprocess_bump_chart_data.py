import pandas as pd

input_file = 'death-rate-by-risk-factor-year.csv'
df = pd.read_csv(input_file)

df['country'] = df['country'].replace('Global', 'World')
filtered_df = df[(df['metric_name'] == 'Rate') & (df['death_cause'] != 'High systolic blood pressure')]


ranked_df = filtered_df.groupby(['year', 'country'])['val'].rank(ascending=False, method='first')
ranked_df = ranked_df.rename('rank').astype(int)

filtered_df = pd.concat([filtered_df, ranked_df], axis=1)
filtered_df = filtered_df.drop(columns={'metric_name'})

output_file = 'rank-death-cause-year.csv'
filtered_df.to_csv(output_file, index=False)
