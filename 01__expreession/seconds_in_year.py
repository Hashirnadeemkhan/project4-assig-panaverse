DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def main():
    seconds_in_year = DAYS_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE
    # Print the result
    print(f"There are {seconds_in_year} seconds in a year!")

if __name__ == '__main__':
    main()    