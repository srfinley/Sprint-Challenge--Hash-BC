#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for index, weight in enumerate(weights):
        hash_table_insert(ht, key=weight, value=index)

    for index, weight in enumerate(weights):
        if hash_table_retrieve(ht, limit - weight) is not None:
            index1 = index
            index2 = hash_table_retrieve(ht, limit - weight)
            if index1 < index2:
                return (index2, index1)
            elif index1 > index2:
                return (index1, index2)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
