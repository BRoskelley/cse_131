# 1. Name:
#      Brighton Roskelley
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      Display a calendar of a month and year that the user has chosen.
# 4. What was the hardest part? Be as specific as possible.
#      There wasn't a hard part of this assignment for me. 
#      I just didnt try to get all of the fail cases to work.
# 5. How long did it take for you to complete the assignment?
#      it took me about 1.5 hours.



def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline

def is_leap_year(user_year):
    is_leap = False
    if user_year % 400 == 0:
        is_leap =  True
    elif user_year % 100 == 0 and user_year % 400 != 0:
        is_leap = False
    elif user_year % 4 == 0 and user_year % 100 != 0:
        is_leap = True
    else:
        is_leap = False
    return is_leap

def check_valid_month(user_month):
    if 1 <= user_month <= 12:
        return False
    else:
        print ("Please enter a month between 1 and 12.")
        return True

def check_valid_year(user_year):
    if user_year >= 1753:
        return False
    else:
        print ("Please enter a year greater that 1752.")
        return True

def get_user_year():
    valid_year = True
    while valid_year:
        user_year = int(input("what year do you want to display? "))
        valid_year = check_valid_year(user_year)
    return (user_year)

def get_user_month():
    valid_month = True
    while valid_month:
        user_month = int(input("what month do you want to display? "))
        valid_month = check_valid_month(user_month)
    return (user_month)

def find_num_days(user_month, user_year):
    total_num_days = 365
    for month in range(1,user_month):
        total_num_days += find_number_days_in_month(month, user_year)
    
    for year in range(1753,user_year):
        if is_leap_year(year):
            total_num_days += 366
        else:
            total_num_days +=365
    return total_num_days

def find_number_days_in_month(user_month, user_year):
    dom = 0
    long_month = [1,3,5,7,8,10,12]
    short_month = [4,6,9,11]
    if user_month in long_month:
        dom = 31
    elif user_month in short_month:
        dom = 30
    elif user_month == 2:
        if is_leap_year(user_year):
            dom = 29
        else:
            dom = 28
    return dom

def find_dow(num_days):
    dow = num_days % 7
    return dow


def main():
    user_month = get_user_month()
    user_year = get_user_year()
    num_days = find_num_days(user_month, user_year)
    dow = find_dow(num_days)
    num_days_in_month = find_number_days_in_month(user_month,user_year)
    display_table(dow, num_days_in_month)
    return 

if __name__ == "__main__":
    main()