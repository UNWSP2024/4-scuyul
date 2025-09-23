# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the
# month and keep a running total. (Enter 0 to exit the loop)
# When the loop finishes, the program should display the amount that the
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         # initialize for while loop
    total = 0.0

    budget = float(input("Enter total amount budget for this month: "))

    spent = input("Enter expense (leave blank to finish): ")

    while spent != "":
        total += float(spent)   # convert input to float before adding
        spent = input("Enter another expense (leave blank to finish): ")

    print("Total expenses:", total)

    if total > budget:
        difference = total - budget
        print("You are over budget by", difference)
    elif total < budget:
        difference = budget - total
        print("You are under budget by", difference)
    else:
        print("You are exactly on budget!")


if __name__ == '__main__':
    main()
