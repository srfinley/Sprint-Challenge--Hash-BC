#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        hash_table_insert(hashtable, key=ticket.source, value=ticket.destination)
    
    airport = hash_table_retrieve(hashtable, "NONE")
    for stop in range(length):
        route[stop] = airport
        airport = hash_table_retrieve(hashtable, airport)

    return route[:-1]
