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
    totalmonths = 0
    totalRain = 0
    years = int(input("How many years: "))
    for i in range(years):
        print("Year:", i + 1)
        for j in range(12):
            rainfall = float(input("Rainfall in the " + str(j + 1) + " Month: "))
            totalRain = totalRain + rainfall
            totalmonths = totalmonths + 1
    print("Total Rainfall:", totalRain)
    print("Total months:", totalmonths)
    print("average monthly rainfall:", totalRain / totalmonths)

if __name__ == '__main__':
    main()
