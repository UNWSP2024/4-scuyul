# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.
def main():
    totalTicket = 0

    while True:
        input("What movie do you want tickets for: ")
        ticketNum = int(input("How many tickets: "))  # convert to int
        totalTicket += ticketNum

        more = input("More tickets (Y/N): ").strip().lower()
        if more != "y":
            break

    print("Total tickets ordered:", totalTicket)

if __name__ == '__main__':
    main()
