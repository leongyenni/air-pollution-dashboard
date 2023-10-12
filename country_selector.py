import pandas as pd


csv_file_path = './data/death-rates-from-air-pollution.csv'

df = pd.read_csv(csv_file_path)

countries_to_select = ['Japan', 'Switzerland', 'Malaysia', 'United States', 'United Kingdom', 'India', 'China', 'World']

selected_countries = df[df['Country'].isin(countries_to_select)]

columns_to_keep = ['Country', 'Year', 'Household air pollution', 'Ambient Particulate Matter Pollution', 'Total', 'Ambient Ozone Pollution']

melted_df = pd.melt(selected_countries, id_vars=['Country', 'Year'], value_vars=columns_to_keep[2:], var_name='Air Pollution Type', value_name='Count')

output_csv_file = './data/cleaned-death-rates-from-air-pollution.csv'

melted_df.to_csv(output_csv_file, index=False)

print(f'Flattened data saved to {output_csv_file}')
