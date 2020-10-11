# U P E R

# U - Understand

# We need to write a function that reconstructs
# our trip from your mass of flight tickets.

# Ticket is a class with a source and destination
# Source represents starting airport
# Destionation represents the next airport (.next)

# The first flight ticket has no source
# The final destination has a source

# Input: Tickets, length
# Output: List of strings with the entire route of the trip.


# P - Plan
# We need to link the tickets together to reconstruct the trip.
# We can hash each ticket such that the starting location is the key
# and the destination is the value.

# E - Execute

#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source  # starting point
        self.destination = destination  # next airport


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    Ticket = {}
    route = []

    for ticket in tickets:
        Ticket[ticket.source] = ticket.destination

    for _ in range(length):
        if not route:
            route.append(Ticket['NONE'])
        else:
            route.append(Ticket[route[-1]])
    return route


test_tickets = [Ticket("NONE", "PDX"),
                Ticket("PDX", "DCA"),
                Ticket("DCA", "NONE")]

print(reconstruct_trip(test_tickets, 3))

# R - Reflect
# Should probably consider setting several alarms
# So you don't scramble your flight tickets to begin with.
