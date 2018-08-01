import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': '/home/wiselap/Machine Learning/bikeshare-2/chicago.csv',
              'new york city': '/home/wiselap/Machine Learning/bikeshare-2/new_york_city.csv',
              'washington': '/home/wiselap/Machine Learning/bikeshare-2/washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user raw_input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid raw_inputs


    # get user raw_input for month (all, january, february, ... , june)


    # get user raw_input for day of week (all, monday, tuesday, ... sunday)
    while True:

        print('-'*40)

        """Taking raw_input from user for city"""
        print('Bike Share Catalog')
        print("")
        print("You can explore Chicago, New York City and Washington");
        print("")



        city = input('Which city would you like to explore?\n').lower()
        print(city)

        if city.lower() in CITY_DATA:
            print('-'*40)
            month = input("Would you like to filter information by month?\nIf 'Yes' Please specify month between January to June \n").lower()
            if month in months or month == 'no':
                print('-'*40)
                day = input("Would you like to filter information by day?\nIf 'Yes' Please specify day\n").lower()
                if day in days or day == 'no':
                    print('-'*40)
                    break;
                else:
                    print('Please enter a valid day!')


            else:
                print('Please enter a valid month!')

        else:
            print('We dont have data for this city.Please enter another city!')



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


    if 'Start Time' in df.columns:
        if noOfNan(df,'Start Time') !=0:
            df['Start Time'].fillna(method = 'bfill',inplace = True)

        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['Month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name

        if month != 'no':
            location_of_month = pd.Index(months).get_loc(month.lower())+1;
            df = df.loc[df['Month'] == location_of_month]

        if day != 'no':
            df = df.loc[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if 'Start Time' in df.columns:

        most_frequent_month = months[df['Month'].mode()[0]-1]
        print("Most frequent month of travel : {}".format(most_frequent_month.title()))


    # display the most common day of week
        most_frequent_day_of_week = df['day_of_week'].mode()[0]
        print("Most frequent day of travel : {}".format(most_frequent_day_of_week))


    # display the most common start hour
        df['hour'] = df['Start Time'].dt.hour
        most_common_start_hour = df['hour'].mode()[0]
        print("Most frequent start time of travel : {}".format(most_common_start_hour))

    else:
        print("Most frequent month of travel : Not Available")
        print("Most frequent day of travel : Not Available")
        print("Most frequent start time of travel : Not Available")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    """
    value_counts return the no of occurence of a element in descending order
    hence first element is the most repeated one
    """
    # display most commonly used start station

    if 'Start Station' in df.columns:
        if noOfNan(df,'Start Station') !=0:
            df['Start Station'].fillna(method = 'bfill',inplace = True)

        value_counts_of_start_station = df['Start Station'].value_counts()
        most_commonly_used_start_station = value_counts_of_start_station.index[0]
        print("Most commonly used start station : {}".format(most_commonly_used_start_station))
    else:
        print("Most commonly used start station : Not Available")


    # display most commonly used end station
    if 'End Station' in df.columns:
        if noOfNan(df,'End Station') != 0:
            df['End Station'].fillna(method = 'bfill',inplace = True)

        value_counts_of_end_station = df['End Station'].value_counts()
        most_commonly_used_end_station = value_counts_of_end_station.index[0]
        print("Most commonly used End Station   : {}".format(most_commonly_used_end_station))
    else:
        print("Most commonly used End Station   : Not Available")

    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    if 'Trip Duration' in df.columns:
        if noOfNan(df,'Trip Duration') != 0:
            df['Trip Duration'].fillna(method = 'bfill',inplace = True)

        total_time_travel = df['Trip Duration'].values.sum()
        mean_travel_time = df['Trip Duration'].mean()

    # display total travel time
        print("Total time travelled : {}".format(total_time_travel))

    # display mean travel time
        print("Mean travel time     : {}".format(mean_travel_time))

    else:
        print("Not Available")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("--------User Types--------")

    if 'User Type' in df.columns:

        if noOfNan(df,'User Type') != 0:
            df['User Type'].fillna(method = 'bfill',inplace = True)

        count_of_user_types = df['User Type'].value_counts().to_frame()
        index = count_of_user_types.index
        for user_type in index:
            print("{} : {} ".format(user_type,count_of_user_types.loc[user_type]['User Type']))

    print("")
    # Display counts of gender
    print("--------Gender Counts--------")
    if 'Gender' in df.columns:

        if noOfNan(df,'Gender') != 0:
            df['Gender'].fillna(method = 'bfill' , inplace = True)

        counts_of_gender = df['Gender'].value_counts().to_frame();
        index = counts_of_gender.index
        for gender in index:
             print("{} : {}".format(gender,counts_of_gender.loc[gender]['Gender']))
    else:
         print("Not Available")


    # Display earliest, most recent, and most common year of birth
    print("")
    print("--------Year of birth--------")
    if 'Birth Year' in df.columns:

        if noOfNan(df,'Birth Year') !=0:
            df['Birth Year'].fillna(method = 'bfill' , inplace = True)

        earliest_year_of_birth = df['Birth Year'].min().astype(np.int64)
        most_recent_year_of_birth = df['Birth Year'].max().astype(np.int64)
        most_common_year_of_birth = df['Birth Year'].mode()[0].astype(np.int64)
        print("Earliest year of birth : {}".format(earliest_year_of_birth))
        print("Most recent year of birth : {}".format(most_recent_year_of_birth))
        print("Most common year of birth : {}".format(most_common_year_of_birth))
    else:
        print("Not Available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def noOfNan(df,column_name):
    null_value_count = df.isnull().sum()
    return null_value_count[column_name]




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
