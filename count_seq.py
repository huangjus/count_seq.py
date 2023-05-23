# Author: Justin Huang
# GitHub username: huangjus
# Date: 5/23/23
# Description: The code defines a generator function called `count_seq` that generates an infinite sequence by
# counting consecutive occurrences of digits in the previous term. The terms are stored in a list and yielded one
# by one. The generator allows for indefinite generation of the sequence, returning the terms as strings.

def count_seq():
    """
    Generate a sequence based on the count of consecutive digits in the previous term.
    """
    yield "2"  # First term is "one 2"
    yield "12"  # Second term is "one 1" followed by "one 2"

    terms = ["2", "12"]  # Initialize the terms list with the first two terms

    while True:
        current_term = ""
        count = 1

        for i in range(len(terms[-1])):
            if i + 1 < len(terms[-1]) and terms[-1][i] == terms[-1][i + 1]:
                count += 1
            else:
                current_term += str(count) + terms[-1][i]
                count = 1

        terms.append(current_term)
        yield current_term
