# Open csv file and read data from a file_path given

import csv

def load_data(file_path):

    with open(file_path, encoding='utf-8') as csv_file:
        # Read a csv file
        csv_reader = csv.reader(csv_file)

         # Display a list of values for each line in the file
        for row in csv_reader:
            print(row)

            
            
            
import csv
#Retrieve a Name of ( Listing, Host name, Description, Host location, and the date the host was created for an individual host by host id )
import csv

def retrieve_data_by_id(file_path):
    
    while True:
        # Prompt user to enter host_id to search for
        host_id = input("Enter Host id to search for (or enter 'quit' to exit): ")
        # Exit loop if user enters 'quit'
        if host_id == 'quit':
            break
        
        # Open csv file and read data from a file
        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)

            # Iterate through the rows in the CSV file
            for row in csv_reader:
                # Check if the host_id in the current row matches the desired host_id
                if row["host_id"] == host_id:
                    # If the host_id matches, print the requested information
                    print("Name of listing:", row["name"])
                    print("Host name:", row["host_name"])
                    print("Description:", row["description"])
                    print("Host location:", row["host_location"])
                    print("Date the host was created:", row["host_since"])
                    break
            else:
                # If no matching host_id was found in the file, print a message to the user
                print("No host found with host_id:", host_id)

                
                
                

# Retrieve host_name, property_type, price, minimum_nights, and maximum_nights of all Airbnb listing for a specified location



def get_listings_by_location(location, file_path):
    # Open the input CSV file
    with open(file_path) as input_file:
        # Create a CSV reader
        csv_reader = csv.DictReader(input_file)

        # Initialize an empty list to store the matching listings
        listings = []

        # Iterate through the rows in the input CSV file
        for row in csv_reader:
            # Check if the location in the current row matches the desired location
            if row["host_location"].lower() == location.lower():
                # If the location matches, extract the requested information and add it to the list
                listing = {
                    "host_name": row['host_name'],
                    "property_type": row['property_type'],
                    "price": row['price'],
                    "minimum_nights": row['minimum_nights'],
                    "maximum_nights": row['maximum_nights']
                }
                listings.append(listing)

        # Return the list of matching listings
        return listings

          
      
        
              
# Retrieve room_type, accommodates, bathrooms, bedroom, and beds of all Airbnb listing for a specified property type

import csv

def get_listings_by_property_type(property_type, file_path):
    results = []
    # Open the input CSV file
    with open(file_path) as input_file:
        csv_reader = csv.DictReader(input_file)
         # Iterate through the rows in the input CSV file
        for row in csv_reader:
             # Check if the location in the current row matches the desired property type
            if row["property_type"] == property_type:
                # If the property type matches, extract the requested information and add it to the list
                results.append({
                    "room_type": row["room_type"],
                    "accommodates": row["accommodates"],
                    "bathrooms_text": row["bathrooms_text"],
                    "bedrooms": row["bedrooms"],
                    "beds": row["beds"]
                })
    # Return the list of matching listings
    return results or None


                
                
# Retrieve specific columns of your choice related to an individual host by location(at least 3 columns and should be different to previous requirements) and also save it with the search name into the directory
# Retrieve Host ID, Location, Last Review, First Review, Host Response Time, and Accommodates for a specified location
import csv
import os

def show_listings_by_location(location, file_path):
    results = []
 # Open the input CSV file
    with open(file_path) as input_file:
        csv_reader = csv.DictReader(input_file)
# Check if the location in the current row matches the desired location
        for row in csv_reader:
        # If the location matches, extract the requested information and add it to the list
            if row["host_location"] == location:
                results.append({
                    # If the location matches, extract the requested information and add it to the list
                    "Host ID": row["host_id"],
                    "Location": row["host_location"],
                    "Last Review": row["last_review"],
                    "First Review": row["first_review"],
                    "Host Response Time": row["host_response_time"],
                    "Accommodates": row["accommodates"]
                })
# Return the list of matching listings
    if not results:
        return None

    dir_name = f"{location}_listings"
    os.makedirs(dir_name, exist_ok=True)

    file_path = os.path.join(dir_name, f"{location}_listings.csv")
    with open(file_path, "w", newline="") as output_file:
        fieldnames = ["Host ID", "Location", "Last Review", "First Review", "Host Response Time", "Accommodates"]
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for result in results:
            csv_writer.writerow(result)
# Return the list of matching listings
    return results





#Load the data from a CSV file into memory using the Pandas module.
import pandas as pd

def read_airbnb_data(file_path):
    df_Airbnb = pd.read_csv(file_path)
    return df_Airbnb.head()                
                

    
                
import pandas as pd
#Identifying the most popular Amenities or features that Airbnb guests are looking for
def get_top_amenities(file_path):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path, header=0)

    # Create a list to hold all the amenities
    amenities = []

    # Iterate over each row of the DataFrame and split the amenities string
    # into a list of amenities, and add each individual amenity to the amenities list
    for index, row in df.iterrows():
        for amenity in row['amenities'].split(","):
            amenities.append(amenity.strip("{}'"))

    # Convert the amenities list to a pandas Series
    amenities_series = pd.Series(amenities)

    # Get the top 50 most common amenities
    top_50_amenities = amenities_series.value_counts().head(50)

    # Return the top 50 most common amenities
    return top_50_amenities





#Analyse the average price of stay in each location groupby location and calculate the mean price for each group
def get_top_locations(file_path):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path, header=0)

    # Group by location and calculate the mean price for each group
    price_by_location = df.groupby('host_location')['price'].mean()

    # Sort the result in descending order and display the top 50 locations
    top_locations = price_by_location.sort_values(ascending=False).head(50)

    # Return the top 50 locations with the highest average prices
    return top_locations





# Analyse the average review scores rating for each location
def get_top_locations_by_review_score(file_path):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path, header=0)

    # Group by location and calculate the mean review scores rating for each group
    rating_by_location = df.groupby('host_location')['review_scores_rating'].mean()

    # Sort the result in descending order and display the top 50 locations
    top_locations = rating_by_location.sort_values(ascending=False).head(50)

    # Return the top 50 locations with the highest average review scores ratings
    return top_locations



# calculate the mean review scores accuracy for each group i.e Analyse the average Minimum Night rating for each location

def calculate_mean_min_nights_by_location(file_path):
    # Load the data into memory
    data = pd.read_csv(file_path)

    # Extract the necessary columns
    df = data[['host_location', 'minimum_nights']]

    # Group the data by location
    grouped_data = df.groupby('host_location')

    # Calculate the mean of minimum_nights for each location group
    mean_minimum_nights = grouped_data['minimum_nights'].mean()

    return mean_minimum_nights





#Display the proportion of number of bedrooms of Airbnb listing using pie chart
import csv
import matplotlib.pyplot as plt

def plot_bedroom_counts():
    # Read the CSV file
    with open('Airbnb_UK_2022.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    # Count the number of listings for each bedroom count
    bedroom_counts = {}
    for row in data:
        bedrooms = row['bedrooms']
        if bedrooms in bedroom_counts:
            bedroom_counts[bedrooms] += 1
        else:
            bedroom_counts[bedrooms] = 1

    # Create a list of labels and values for the pie chart
    labels = []
    values = []
    for key, value in bedroom_counts.items():
        if key != '':
            labels.append(f"{key} bedroom(s)")
            values.append(value)

    # Create the pie chart
    fig = plt.figure(figsize=(10,8))
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.legend(loc="best",bbox_to_anchor=(1.2,1))
    plt.title("Proportion of Number of Bedrooms in Airbnb Listings")
    plt.legend()
    plt.axis('equal')
    plt.show()


#Display the proportion of number of bedrooms of Airbnb listing using pie chart; to save the fig in the directory

import csv
import matplotlib.pyplot as plt

def generate_bedroom_pie_chart(file_path):
    # Read the CSV file
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    # Count the number of listings for each bedroom count
    bedroom_counts = {}
    for row in data:
        bedrooms = row['bedrooms']
        if bedrooms in bedroom_counts:
            bedroom_counts[bedrooms] += 1
        else:
            bedroom_counts[bedrooms] = 1

    # Create a list of labels and values for the pie chart
    labels = []
    values = []
    for key, value in bedroom_counts.items():
        if key != '':
            labels.append(f"{key} bedroom(s)")
            values.append(value)

    # Create the pie chart
    fig = plt.figure(figsize=(10,8))
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.legend(loc="best",bbox_to_anchor=(1.2,1))
    plt.title("Proportion of Number of Bedrooms in Airbnb Listings")
    plt.axis('equal')
    plt.legend()
    
    # Save the chart to a file
    fig.savefig('bedroom_pie_chart.png')
    
    # Return the chart
    return fig



#Display the number of listings for each room type using bar chart
import csv
import matplotlib.pyplot as plt

def plot_room_type_counts():
    # Read the CSV file
    with open('Airbnb_UK_2022.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    # Count the number of listings for each room type
    room_type_counts = {}
    for row in data:
        room_type = row['room_type']
        if room_type in room_type_counts:
            room_type_counts[room_type] += 1
        else:
            room_type_counts[room_type] = 1

    # Create a bar chart
    plt.bar(room_type_counts.keys(), room_type_counts.values())
    plt.title("Number of Listings for Each Room Type")
    plt.xlabel("Room Type")
    plt.ylabel("Number of Listings")
    plt.show()


    
 #Display the relationship between accommodates and price using scatter plot  
import csv
import matplotlib.pyplot as plt

def generate_accommodates_price_scatter(file_path):
    # Read the CSV file
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    # Extract the accommodates and price data
    accommodates = []
    price = []
    for row in data:
        if row['accommodates'] != '' and row['price'] != '':
            accommodates.append(int(row['accommodates']))
            price.append(float(row['price'].replace('£', '').replace(',', '')))

    # Create a scatter plot
    fig = plt.figure(figsize=(10,8))
    plt.scatter(accommodates, price)
    plt.title("Relationship between Accommodates and Price")
    plt.xlabel("Accommodates")
    plt.ylabel("Price (£)")
    
    # Save the chart to a file
    fig.savefig('accommodates_price_scatter.png')
    
    # Return the chart
    return fig





#Display Airbnb prices from 2019 - 2022 with line chart using subplots (one year per plot)
import pandas as pd
import matplotlib.pyplot as plt

def plot_airbnb_prices_by_year():
    # Load the data into a pandas DataFrame
    df = pd.read_csv('Airbnb_UK_2022.csv')

    # Convert the date column to datetime format
    df['host_since'] = pd.to_datetime(df['host_since'])

    # Set the date column as the index of the DataFrame
    df.set_index('host_since', inplace=True)

    # Create a figure with 4 subplots, one for each year
    fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(10, 20))

    # Loop over each year and plot the Airbnb prices
    for i, year in enumerate(range(2019, 2023)):
        year_df = df[df.index.year == year]
        year_df['price'].plot(ax=axes[i])
        axes[i].set_title('Airbnb Prices in {}'.format(year), pad=20) # Add padding to the title
        axes[i].set_xlabel('Date')
        axes[i].set_ylabel('Price')
        

    # Add some space between the subplots
    fig.subplots_adjust(hspace=0.5)

    # Display the plots
    plt.show()


    
    
    
    #display the average price per night for each property type.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_average_price_by_property_type(file_path):
    """
    Plot the Average price per night for each property type.

    Args:
        file_path (str): The file path of the CSV containing the data.

    Returns:
        None
    """

    # Load data
    data = pd.read_csv(file_path)

    # Group data by property type and calculate the average price per night
    grouped_data = data.groupby("property_type")["price"].mean().reset_index()

    # Create a bar chart of the average price per property type
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 8))
    ax = sns.barplot(x="property_type", y="price", data=grouped_data)
    plt.title("Average Price per Property Type on Airbnb UK 2022")
    plt.xlabel("Property Type")
    plt.ylabel("Average Price per Night (£)")

    # Add a horizontal line to indicate the overall average price
    overall_avg_price = data["price"].mean()
    ax.axhline(y=overall_avg_price, color='r', linestyle='--')
    plt.text(-0.2, overall_avg_price + 5, f'Overall Avg. Price: £{overall_avg_price:.2f}', fontsize=12)

    # Rotate x-axis labels
    plt.xticks(rotation=45, ha='right')

    plt.show()

