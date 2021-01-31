import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = []
    city = input('We are excited to explore some data. Whcih city should we dig int?: chicago, new york city, or washington?\n').lower()

    while city not in ('chicago', 'new york city', 'washington'):
        print('\nI didn\'t understand your city. Let\'s try that again.')
        city = input('\nWhich city would you like to explore: chicago, new york city, or washington?\n').lower()
        cities.append(city)
    # TO DO: get user input for month (all, january, february, ... , june)
    months = []
    month = input('Which month would you like to explore: all, january, february, march ....?\n').lower()

    while month not in ('all, january, february, march, april, may, june, july, august, september, october, november, december'):
        print('\nI didn\'t understand your month. Let\'s try that again.')
        month = input('\nWhich month would you like to explore: all, january, february, march ....?\n').lower()
        months.append(month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = []
    day = input('Which day would you like to explore: all, monday, tuesday...?\n').lower()

# Start a loop that will run until the user enters 'quit'.
    while day not in ('all, monday, tuesday, wednseday, thursday, friday, saturday, sunday'):
        print('\nI didn\'t understand your day. Let\'s try that again.')
        day = input('\nWhich day would you like to explore: all, monday, tuesday...?\n').lower()
        days.append(day)
             
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month_of_year'] = df['Start Time'].dt.month
    df['day-week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        df['month_of_year'].filter(month)

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df['day-week'].filter(day)
    
    return df
"""
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

#####Defining Statistics###########
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # find the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)

    # TO DO: display the most common day of week
    # extract day from the Start Time column to create a day column
    df['day'] = df['Start Time'].dt.day
    # find the most common day
    common_day = df['day'].mode()[0]
    print('Most Common Day:', common_day)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common month
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most common start station is:", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("The most common end station is:", common_end_station)

   
    # TO DO: display most frequent combination of start station and end station trip
    df['common_start_end_station'] = df['Start Station'].map(str) + ' & ' + df['End Station']
    most_popular_start_end = df['common_start_end_station'].value_counts().idxmax()
    print("The most common start and end station combination is: {}n".format(most_popular_start_end))
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()/86400
    print("Total travel time:", total_travel, "days")
    
    # TO DO: display mean travel time
    average_travel = df['Trip Duration'].mean()/60
    print("Average travel time:", average_travel, "minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    start_time = time.time()
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    # iteratively print out the total numbers of user types 
    for total, user_count in enumerate(user_counts):
        print("  {} - {}\n".format(user_counts.index[total], user_count))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    #check to ensure that the dataset has a gender column
    if 'Gender' in df.columns:
        user_stats_genders(df)
    else: 
        print("No Gender Stats Present\n")
    #TO DO: Display counts of gender
def user_stats_genders(df):
    start_time = time.time()
    
    gender_counts = df['Gender'].value_counts()
    # iteratively print out the total numbers of gender types 
    for total, gender_count in enumerate(gender_counts):
        print("  {} - {}\n".format(gender_counts.index[total], gender_count))
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    #check to ensure that the dataset has a gender column
    if 'Birth Year' in df.columns:
        user_stats_birthyear(df)
    else: 
        print("No Birthyear Stats Present")
    # TO DO: Display earliest, most recent, and most common year of birth
def user_stats_birthyear(df):
    start_time = time.time()

    most_common_birth_year = int(df['Birth Year'].value_counts().idxmax())
    most_recent_birth_year = int(df['Birth Year'].max())
    earliest_birth_year = int(df['Birth Year'].min())

    print("  Most common birth year:", most_common_birth_year)
    print("\n  Most recent birth year:", most_recent_birth_year)
    print("\n  Earliest birth year:", earliest_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
####
def display_data(df):
    display = input('\nWould you like to view individual trip data? Type \'yes\' or \'no\'.\n').lower()
    while display == "yes":
        x = 0
        y = 5
        while x < len(df.index):
            x = x + 5
            y = y + 5
            print(df.iloc[x:y])
            if display == "no":
                break
            
            display = input('\nWould you like to view more individual trip data? Type \'yes\' or \'no\'.\n').lower()
            while display not in ('yes', 'no'):
                display = input('\nI did not understand. Can you re-enter? \'yes\' or \'no\'.\n').lower()
                if display == "no":
                    break
    if display == "no":
        return
    while display not in ('yes', 'no'):
        display = input('\nI did not understand. Can you re-enter? \'yes\' or \'no\'.\n').lower()
   
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
   
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
