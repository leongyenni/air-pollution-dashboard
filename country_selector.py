import pandas as pd


csv_file_path = './data/death-rates-from-air-pollution.csv'

df = pd.read_csv(csv_file_path)

countries_to_select = ['Japan', 'Switzerland', 'Malaysia', 'United States', 'United Kingdom', 'India', 'China', 'World']

selected_countries = df[df['Country'].isin(countries_to_select)]
selected_countries = selected_countries.rename(columns={'Household air pollution': 'Household Air Pollution'})


columns_to_keep = ['Country', 'Year', 'Household Air Pollution', 'Ambient Particulate Matter Pollution', 'Ambient Ozone Pollution']

melted_df = pd.melt(selected_countries, id_vars=['Country', 'Year'], value_vars=columns_to_keep[2:], var_name='Air Pollution Type', value_name='Count')

selected_year_df = melted_df[melted_df['Year'] == 2019]


# output_csv_file = './data/cleaned-death-rates-from-air-pollution.csv'

# selected_year_df.to_csv(output_csv_file, index=False)

# print(f'Flattened data saved to {output_csv_file}')

output_json_file = './data/cleaned-death-rates-from-air-pollution.json'

selected_year_df.to_json(output_json_file, orient='records')

print(f'Filtered and renamed data saved to {output_json_file}')
