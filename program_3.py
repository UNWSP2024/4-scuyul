# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    # Repeat 5 times
    years = int(input("How many years: "))
    for i in range(years):
        print("Outer Debug loop #", i + 1)
        for j in range(12):
            print("Month loop #", i + 1)
            rainfall = input("Rainfall in the", i + 1, "Month: ")




if __name__ == '__main__':
    main()