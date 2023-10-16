import pandas as pd

# Read the data from the CSV file
data = {
    'Entity': ['Ammonia', 'NMVOC', 'Nitrogen oxides', 'PM10', 'PM2.5', 'Sulphur dioxide'],
    'Year': [2016, 2016, 2016, 2016, 2016, 2016],
    'Agriculture': [253000, 117500, 7200, 17000, 4300, 0],
    'Energy production': [200, 4000, 199700, 4600, 3600, 66800],
    'Fugitive emissions': [200, 129300.00000000001, 2000, 1900, 1200, 2500],
    'Industrial processes': [3800, 443000, 1300, 53200, 13900, 8600],
    'Manufacturing industry & construction': [2100, 19400, 139100, 18000, 17400, 38700],
    'Military aircraft and naval shipping': [0, 600, 12500, 200, 200, 1500],
    'Non-road transport': [12900, 12500, 137900, 3900, 3700, 13400],
    'Other': [4400, 3600, 200, 200, 100, 0],
    'Road transport': [2200, 31800, 299800, 19900, 13400, 1300],
    'Small non-road mobile sources & machinery': [10100, 50400, 91800, 47600, 46600, 45800],
    'Waste': [0, 6500, 1400, 4000, 3600, 700]
}

df = pd.DataFrame(data)

# Fill missing values with 0
df = df.fillna(0)

# Calculate the total emissions for each entity
total_emissions = df.iloc[:, 3:].sum(axis=1)

# Calculate the percentage of each entity's emissions
percentage_emissions = (total_emissions / total_emissions.sum()) * 100

# Create a DataFrame for the percentage emissions
percentage_df = pd.DataFrame({
    'Entity': df['Entity'],
    'Percentage': percentage_emissions
})

# Format the percentage values to two decimal places
percentage_df['Percentage'] = percentage_df['Percentage'].apply(lambda x: f"{x:.2f}")

# Save the percentage emissions to a new CSV file
output_csv = 'pollutants_percentage_emissions.csv'
percentage_df.to_csv(output_csv, index=False)
