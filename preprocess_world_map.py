import csv
from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha2, convert_continent_code_to_continent_name


def get_continent(country_name):
    if country_name.lower() == 'east timor':
        return 'Asia'

    try:
        country_code = country_name_to_country_alpha2(country_name)
        continent_code = country_alpha2_to_continent_code(country_code)
        continent_name = convert_continent_code_to_continent_name(
            continent_code)

        return continent_name
    except Exception as e:
        pass
    return 'Unknown'


# Read the data.csv file and filter rows with null values
filtered_data = []

with open('cleaned-share-deaths-air-pollution.csv', mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        country = row['Country']
        share_of_total_deaths = row['Share_of_total_deaths']
        year = row['Year']

        if (year == "2019"):
            filtered_data.append({
                'Country': country,
                'Share_of_total_deaths': float(share_of_total_deaths),
                'Year': int(year)
            })


# Group filtered data by continent
continent_data = {}

for row in filtered_data:
    country = row['Country']
    continent = get_continent(country)

    if continent not in continent_data:
        continent_data[continent] = []

    continent_data[continent].append(row)

# Write the grouped and filtered data to a new CSV file
output_file = 'year-share-deaths-air-pollution.csv'
with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Country',
                  'Share_of_total_deaths',
                  'Year',
                  'Continent']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for continent, countries in continent_data.items():
        for country_info in countries:
            country_info['Continent'] = continent
            writer.writerow(country_info)

print(f'Filtered and grouped data saved to "{output_file}".')
