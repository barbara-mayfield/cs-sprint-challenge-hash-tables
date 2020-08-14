#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source  # starting airport
        self.destination = destination  # next airport


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
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
