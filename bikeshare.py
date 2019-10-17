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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        try:
            city = input('\nWhat city datas would you like to view ? Enter the name (chicago, new york city, washington): ').lower()
        except:
            print("Oops! You haven't entered a city name.")
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    while month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
        try:
            month = input('\nView data for wich month ? Enter the name (all, january, february, march, april, may, june): ').lower()
        except:
            print("Oops! You haven't entered a month name.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
        try:
            day = input('\nView data for wich day ? Enter the name (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ').lower()
        except:
            print("Oops! You haven't entered a day of week name.")

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
    df['hour'] = df['Start Time'].dt.hour
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

    # TO DO: display the most common month
    print('\nMost common month: {}'.format(df['month'].value_counts().idxmax()))

    # TO DO: display the most common day of week
    print('\nMost common day of week: {}'.format(df['day_of_week'].value_counts().idxmax()))

    # TO DO: display the most common start hour
    print('\nMost common start hour: {}'.format(df['hour'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nMost commonly used start station: {}'.format(df['Start Station'].value_counts().idxmax()))

    # TO DO: display most commonly used end station
    print('\nMost commonly used end station: {}'.format(df['End Station'].value_counts().idxmax()))

    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost frequent combination of start station and end station: {}'.format(df.groupby(['Start Station','End Station']).size().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nTotal of travel time : {}\n'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('\nMean of travel time : {}\n'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nUser types counts : \n{}'.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    try:
        print('\nGender counts : \n{}'.format(df['Gender'].value_counts()))
    except:
        print('\nGender counts : None')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('\nEarliest year of birth : \n{}'
            .format(df[df['Birth Year'] == df['Birth Year'].min()]['Birth Year']))
    except:
        print('\nEarliest year of birth : None')

    try:
        print('\nMost common year of birth : \n{}'
            .format(df['Birth Year'].value_counts().idxmax()))
    except:
        print('\nMost common year of birth : None')

    try:
        print('\nMost recent year of birth : \n{}'
            .format(df[df['Birth Year'] == df['Birth Year'].max()]['Birth Year']))
    except:
        print('\nMost recent year of birth : None')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_data(df):
	"""Displays datas on bikeshare users."""

    row_count = 0
    while True:
        print_again = input('\nWould you like to print datas ? Enter yes or no. \n').lower()
        if print_again != 'yes':
            break
        print(df.iloc[row_count:row_count+5, 0:9])
        row_count += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
