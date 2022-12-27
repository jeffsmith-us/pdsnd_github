import time
import pandas as pd

city_data = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    validvalueerror = "{} is not a valid value. Please try again.\n{}\n"
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_prompt = "Please enter the name of the city of interest."
    city_validvalues = "(Valid entries are Chicago, New York City, or Washington.)"
    city = input("\n{}\n{}\n".format(city_prompt, city_validvalues)).title()
    
    while city not in city_data:
        city = input(validvalueerror.format(city, city_validvalues)).title()

    # get user input for month (all, january, february, ... , june)
    month_validvaluelist = ["All", "January", "February", "March", "April", "May", "June"]
    month_prompt = "Please enter the month of interest or 'All' for all months."
    month_validvalues = "(Valid entries are full month names from January through June or 'All'.)"
    month = input("\n{}\n{}\n".format(month_prompt, month_validvalues)).title()
    
    while month not in month_validvaluelist:
        month = input(validvalueerror.format(month, month_validvalues)).title()
    
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_validvaluelist = ["All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_prompt = "Please enter the day of week of interest or 'All' for all days of the week."
    day_validvalues = "(Valid entries are full day names from Monday through Sunday or 'All'.)"
    day = input("\n{}\n{}\n".format(day_prompt, day_validvalues)).title()
    
    while day not in day_validvaluelist:
        day = input(validvalueerror.format(day, day_validvalues)).title()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city, extracts useful values, and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(city_data[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract useful values from Start Time to create new columns
    df['month_name'] = df['Start Time'].dt.month_name()
    df['day_name'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'All':  
        # filter by month to create the new dataframe
        df = df[df['month_name'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_name'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_mode = df['month_name'].mode()[0]
    print("The most common month for travel was {}.\n".format(month_mode))

    # display the most common day of week
    day_mode = df['day_name'].mode()[0]
    print("The most common day of the week for travel was {}.\n".format(day_mode))

    # display the most common start hour
    start_hour_mode = df['start_hour'].mode()[0]
    print("The most common hour for starting travel was {}.\n".format(start_hour_mode))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station_mode = df['Start Station'].mode()[0]
    print("The most common starting station was {}.\n".format(start_station_mode))

    # display most commonly used end station
    end_station_mode = df['End Station'].mode()[0]
    print("The most common ending station was {}.\n".format(end_station_mode))

    # display most frequent combination of start station and end station trip
    station_combo_mode = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print("The most common combination of starting and ending station was {}.\n".format(station_combo_mode))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    duration_total = df['Trip Duration'].sum()
    print("The total trip duration for the data set was {} seconds.\n".format(duration_total))

    # display mean travel time
    duration_mean = df['Trip Duration'].mean()
    print("The average trip duration was {} seconds.\n".format(duration_mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    usertype_count = df['User Type'].value_counts()
    print("The counts of different user types are specified below:\n{}\n".format(usertype_count))

    # Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print("The counts of different genders are specified below:\n{}\n".format(gender_count))
    else:
        print("Gender counts not available for this data set.\n")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        birthyear_min = int(df['Birth Year'].min())
        birthyear_max = int(df['Birth Year'].max())
        birthyear_mode = int(df['Birth Year'].mode()[0])
        print("The earliest birth year was {}.\n".format(birthyear_min))
        print("The most recent birth year was {}.\n".format(birthyear_max))
        print("The most common birth year was {}.\n".format(birthyear_mode))
    else:
        print("Birth year statistics are not available for this data set.\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def print_rawdata(df):
    """
    Prompts user to optionally display raw data from dataframe, five lines
    at a time.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame with city data as loaded and filtered by load_data function.

    Returns
    -------
    None.

    """

    # Drop columns added in load_data to get back to original data set for display
    df = df.drop(['month_name', 'day_name', 'start_hour'], axis = 1)
    
    # Initialize startrow to first row
    startrow = 0
    
    # Prompt to see if user wants to display data
    show_data = input("\nWould you like to view the raw data? Enter 'yes' to display raw data or anything else to exit.\n").lower()
    
    while show_data == 'yes':
        # Set stoprow to show five more rows or to end of dataframe, whichever is lowest
        stoprow = min(startrow+5, len(df))
        print("\nDisplaying rows {} through {} of {} total rows of raw data:\n".format(startrow+1, stoprow, len(df)))
        # Converts raw output to string, wrapped at 80 chars for more legible output
        print(df[startrow:stoprow].to_string(line_width=80))
        
        if stoprow == len(df):
            # Stops the loop if we've shown all rows
            print("All {} rows of raw data have been displayed!\n".format(len(df)))
            break
        else:
            # Provide option to continue the loop and set startrow where we left off
            show_data = input("\nWould you like to view more raw data? Enter 'yes' to display raw data or anything else to exit.\n").lower()
            startrow = stoprow
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print_rawdata(df)

        restart = input("\nWould you like to restart? Enter 'yes' to continue or anything else to exit.\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
