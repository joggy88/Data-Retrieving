LINE_WIDTH = 85

def started(msg=""):
    output = f"Operation started: {msg}..."
    dashes = "-" * LINE_WIDTH
    print(f"{dashes}\n{output}\n")

def completed():
    dashes = "-" * LINE_WIDTH
    print(f"\nOperation completed.\n{dashes}\n")

def error(msg):
    print(f"Error! {msg}\n")


def display_main_menu():
    
    print("Welcome to Airbnb Data Analysis Tool!")
    print("1. CSV Module")
    print("2. Pandas Module")
    print("3. Visualization Module")
    print("4. Exit")

def display_csv_module_options():
    print("CSV Module Menu:")
    print("1. Retrieve data for an individual host by host_id")
    print("2. Retrieve data for all listings for a specified location")
    print("3. Retrieve data for all listings for a specified property type")
    print("4. Retrieve data for a specified location")
    print("5. Back to main menu")

def display_pandas_module_options():
    print("Pandas Module Menu:")
    print("1. Identify the most popular amenities or features")
    print("2. Analyze the average price of stay in each location")
    print("3. Analyze the average review scores rating for each location")
    print("4. Analyze the average minimum night rating for each location")
    print("5. Back to main menu")

def display_visualization_module_options():
    print("Visualization Module Options:")
    print("1. Display proportion of number of bedrooms using a pie chart")
    print("2. Display count of each room type using a bar chart")
    print("3. Display scatter plot of accommodates vs. price")
    print("4. Display line plot of Airbnb prices by year")
    print("5. Display bar chart of average price by property type")
    print("6. Back to main menu")

def retrieve_data_by_id(file_path):
    
    while True:
        host_id = input("Enter Host id to search for (or enter 'quit' to exit): ")
        if host_id == 'quit':
            break

        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row["host_id"] == host_id:                   
                   
                    print("Name of listing:".ljust(25), row["name"])
                    print("Host name:".ljust(25), row["host_name"])
                    print("Description:".ljust(25), row["description"])
                    print("Host location:".ljust(25), row["host_location"])
                    print("Date the host was created:".ljust(25), row["host_since"])
            else:
                print("No host found with host_id:", host_id)

def get_listings_by_location(location, file_path):
    with open(file_path) as input_file:
        csv_reader = csv.DictReader(input_file)
        listings = []
        for row in csv_reader:
            
            if row["host_location"].lower() == location.lower():
                
                listing = {
                    "host_name": row['host_name'],
                    "property_type": row['property_type'],
                    "price": row['price'],
                    "minimum_nights": row['minimum_nights'],
                    "maximum_nights": row['maximum_nights']
                }
                listings.append(listing)
        return listings

def get_listings_by_property_type(property_type, file_path):
    property_type = input("Enter property type to search for: ")
    results = []
    with open(file_path, "r") as input_file:
        csv_reader = csv.DictReader(input_file)
        for row in csv_reader:
            if row["property_type"] == property_type:
                results.append({
                    "room_type": row["room_type"],
                    "accommodates": row["accommodates"],
                    "bathrooms_text": row["bathrooms_text"],
                    "bedrooms": row["bedrooms"],
                    "beds": row["beds"]
                })

    return results or None

def show_listings_by_location(location, file_path):
    results = []
    with open(file_path) as input_file:
        csv_reader = csv.DictReader(input_file)
        for row in csv_reader:
            if row["host_location"] == location:
                results.append({
                    "Host ID": row["host_id"],
                    "Location": row["host_location"],
                    "Last Review": row["last_review"],
                    "First Review": row["first_review"],
                    "Host Response Time": row["host_response_time"],
                    "Accommodates": row["accommodates"]
                })
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
            
            
            
def get_top_amenities(file_path):
    df = pd.read_csv(file_path, header=0)
    amenities = []
    for index, row in df.iterrows():
        for amenity in row['amenities'].split(","):
            amenities.append(amenity.strip("{}'"))
    amenities_series = pd.Series(amenities)
    top_50_amenities = amenities_series.value_counts().head(50)
    print("Top 50 most common amenities:")
    print(top_50_amenities)
    
    
def get_top_locations(file_path):
    df = pd.read_csv(file_path, header=0)
    price_by_location = df.groupby('host_location')['price'].mean()
    top_locations = price_by_location.sort_values(ascending=False).head(50)
    return top_locations
    
    
def get_top_locations_by_review_score(file_path):
    df = pd.read_csv(file_path, header=0)
    rating_by_location = df.groupby('host_location')['review_scores_rating'].mean()
    top_locations = rating_by_location.sort_values(ascending=False).head(50)
    return top_locations


def calculate_mean_min_nights_by_location(file_path):
    data = pd.read_csv(file_path)
    df = data[['host_location', 'minimum_nights']]
    grouped_data = df.groupby('host_location')
    mean_minimum_nights = grouped_data['minimum_nights'].mean()
    return mean_minimum_nights


def generate_bedroom_pie_chart(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    bedroom_counts = {}
    for row in data:
        bedrooms = row['bedrooms']
        if bedrooms in bedroom_counts:
            bedroom_counts[bedrooms] += 1
        else:
            bedroom_counts[bedrooms] = 1
    labels = []
    values = []
    for key, value in bedroom_counts.items():
        if key != '':
            labels.append(f"{key} bedroom(s)")
            values.append(value)
    fig = plt.figure(figsize=(10,8))
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.legend(loc="best",bbox_to_anchor=(1.2,1))
    plt.title("Proportion of Number of Bedrooms in Airbnb Listings")
    plt.axis('equal')
    plt.legend()
    
    # Save the chart to a file
    fig.savefig('bedroom_pie_chart.png')
    return fig


def plot_room_type_counts():
    with open('Airbnb_UK_2022.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    room_type_counts = {}
    for row in data:
        room_type = row['room_type']
        if room_type in room_type_counts:
            room_type_counts[room_type] += 1
        else:
            room_type_counts[room_type] = 1
    plt.bar(room_type_counts.keys(), room_type_counts.values())
    plt.title("Number of Listings for Each Room Type")
    plt.xlabel("Room Type")
    plt.ylabel("Number of Listings")
    plt.show()
    
    
def generate_accommodates_price_scatter(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    accommodates = []
    price = []
    for row in data:
        if row['accommodates'] != '' and row['price'] != '':
            accommodates.append(int(row['accommodates']))
            price.append(float(row['price'].replace('£', '').replace(',', '')))
    fig = plt.figure(figsize=(10,8))
    plt.scatter(accommodates, price)
    plt.title("Relationship between Accommodates and Price")
    plt.xlabel("Accommodates")
    plt.ylabel("Price (£)")
    
    # Save the chart to a file
    fig.savefig('accommodates_price_scatter.png')
    return fig



def plot_airbnb_prices_by_year():
    df = pd.read_csv('Airbnb_UK_2022.csv')
    df['host_since'] = pd.to_datetime(df['host_since'])
    df.set_index('host_since', inplace=True)
    fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(10, 20))
    for i, year in enumerate(range(2019, 2023)):
        year_df = df[df.index.year == year]
        year_df['price'].plot(ax=axes[i])
        axes[i].set_title('Airbnb Prices in {}'.format(year), pad=20)
        axes[i].set_xlabel('Date')
        axes[i].set_ylabel('Price')
    fig.subplots_adjust(hspace=0.5)
    plt.show()

    
    
def plot_average_price_by_property_type(file_path):
    """
    Plot the Average price per night for each property type.

    Args:
        file_path (str): The file path of the CSV containing the data.

    Returns:
        None
    """

    data = pd.read_csv(file_path)
    grouped_data = data.groupby("property_type")["price"].mean().reset_index()
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 8))
    ax = sns.barplot(x="property_type", y="price", data=grouped_data)
    plt.title("Average Price per Property Type on Airbnb UK 2022")
    plt.xlabel("Property Type")
    plt.ylabel("Average Price per Night (£)")
    overall_avg_price = data["price"].mean()
    ax.axhline(y=overall_avg_price, color='r', linestyle='--')
    plt.text(-0.2, overall_avg_price + 5, f'Overall Avg. Price: £{overall_avg_price:.2f}', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.show()

