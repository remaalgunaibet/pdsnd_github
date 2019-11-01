import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

global_city = '' #This is needed to hold the name of the city globally through the whole code file
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    global global_city
    name = input('What is your name? ')
    print('Hello! ' + name + ' Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('Choose one of the following cities: Chicago, New York, or Washington.\n==> ').lower()
        if(city == 'chicago'):
            global_city = 'chicago'
            break
        elif(city == "new york"):
            city = 'new york city'
            global_city = 'new york'
            break
        elif(city == 'washington'):
            global_city = 'washington'
            break
        else:
            city = input('Please try again. Choose one of the following cities: Chicago, New York, or Washington.\n==> ').lower()

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Choose all or specify a month: January, February, ... , December.\n==> ').lower()
        if(month == 'january'):
            break
        elif(month == 'february'):
            break
        elif(month == 'march'):
            break
        elif(month == 'april'):
            break
        elif(month == 'may'):
            break
        elif(month == 'june'):
            break
        elif(month == 'all'):
            break
        else:
            month = input('Please try again. Choose all or specify a month: January, February, ... , December.\n==> ').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Choose all or specify a day: Monday, Tuesday, ... , Sunday.\n==> ').lower()
        if(day == 'monday'):
            break
        elif(day == 'tuesday'):
            break
        elif(day == 'wednesday'):
            break
        elif(day == 'thursday'):
            break
        elif(day == 'friday'):
            break
        elif(day == 'saturday'):
            break
        elif(day == 'sunday'):
            break
        elif(day == 'all'):
            break
        else:
            day = input('Choose all or specify a day: Monday, Tuesday, ... , Sunday.\n==> ').lower()

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Popular Month: '+ format(popular_month))

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Popular Day: "+ popular_day)

    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['start_hour'].mode()[0]
    print("Popular Start Hour: "+ format(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Populat Start Station: " + popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Populat End Station: " + popular_end_station)

    # display most frequent combination of start station and end station trip
    df['station_combo'] = df['Start Station'] + " Station and " + df['End Station'] + " Station"
    print("Popular Comination of Start and End Station: " + df['station_combo'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ' + format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: '+ format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts Based on User Types: ")
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender

    if(global_city != 'washington'):
        print("Counts Based on Gender: ")
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = int(df['Birth Year'].min(axis=0, skipna=True))
        most_recent_birth_year = int(df['Birth Year'].max(axis=0, skipna=True))
        print("Earliest Birth Year: " + format(earliest_birth_year))
        print("Most Recent Birth Year: " + format(most_recent_birth_year))
        print("Common Birth Year: " + format(int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    temp = ''
    while True:
        temp = input('Do you want to see raw data? (Yes/No)\n==> ').lower()
        if(temp == 'yes'):
            print(df.iloc()[0:5])
            break
        elif(temp == 'no'):
            break
        else:
            print('Invalid input. Please answer with yes or no.')
    count = 5
    if(temp != 'no'):
        while True:
            temp = input('Do you want to see more 5 lines of raw data? (Yes/No)\n==> ').lower()
            if(temp == 'yes' and (count+5) < len(df)):
                print(df.iloc()[count:(count+5)])
                count+=1
            elif(temp == 'no'):
                print('Ok.')
                break
            else:
                print('Invalid input. Please answer with yes or no.')


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
