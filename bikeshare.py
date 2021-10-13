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
    # gets user input for city (chicago, new york city, or washington)
    correct = True
    cities = ('chicago', 'new york city', 'washington')
    while correct == True:
        city = input('Hello! Let\'s explore some US bikeshare data!\nWhich city would you like to choose Chicago, New York City, or Washington?\n').lower()
        if city not in cities:
            print('\nNot a valid city name please try again\n')
            continue
        else:
            break
        
    # gets user input for month
    
    months = ('january','february','march','april','may','june', 'all')
    while correct == True:
        month = input('which month? January, February, March, April, May, June or all\n').lower()
        if month not in months:
            print('\nNot a valid month please try again\n')
            continue
        else:
            break
        
    # gets user input for day of week
    
    days = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all')
    while correct == True:
        day = input('which day? please type a day Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all\n').lower()
        if day not in days:
            print('\nNot a valid day of the week please try again\n')
            continue
        else:
            break
        
        
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
    df = pd.read_csv(CITY_DATA[city])

 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['DayOweek'] = df['Start Time'].dt.weekday_name

   
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]


    if day != 'all':
        df = df[df['DayOweek'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # gets the most common month
    common_month = df['Month'].mode()[0]
    print('the most common month is:', common_month)

    # gets the most common day of week
    common_day = df['DayOweek'].mode()[0]
    print('the most common day of the weeek is:', common_day)

    # gets the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('the most common hour is', common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # gets most commonly used start station
    commonStartStation = df['Start Station'].mode()[0]
    print('Most commonly used start station:', commonStartStation)

    # gets most commonly used end station
    commonEndStation = df['End Station'].mode()[0]
    print('Most commonly used end station:', commonEndStation)

    # gets most frequent combination of start and end station (trip)
    df['Frequent Trip'] = df['Start Station'] + ' to ' + df['End Station']
    commonTrip = df['Frequent Trip'].mode()[0]
    print('Most common trip:', commonTrip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # gets total travel time
    print('the total travel time is:', df['Trip Duration'].sum())
    
    # gets mean travel time
    meantravel =  df['Trip Duration'].mean()
    print('the mean travel time is:', meantravel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # gets counts of user types
    accounttypes = df['User Type'].value_counts()
    print('the number of users who have each different type of account are:', accounttypes)
    
    try:
        # gets counts of gender
        gendernumber = df['Gender'].value_counts()
        print('The number of people of each gender:', gendernumber)
    except KeyError:
        print('no gender data could be found')
    
    try:
        # gets earliest, most recent, and most common year of birth
        print('the most recent birth day year was:', df['Birth Year'].min())
    except KeyError:
        print('no Birth year data could be found')

    try:    
        print('the most earliest day year was:',df['Birth Year'].max())
    except KeyError:
        print('no Birth year data data could be found')

    try:    
        commonbirthyear = df['Birth Year'].mode()[0]
        print('the most common birth day year was:', commonbirthyear)
    except KeyError:
        print('no Birth year data could be found')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def  display_data(df):
    ShowDataQ = input('\nDo you want to see five rows of raw data? yes or no\n').lower()
    if ShowDataQ != 'no':
        i = 0
        while (i < df['Start Time'].count() and ShowDataQ != 'no'):
            print(df.iloc[i:i+5])
            i += 5
            MoreDataQ = input('\nWould you like to see 5 more rows of data? yes or no\n').lower()
            if MoreDataQ != 'yes':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
