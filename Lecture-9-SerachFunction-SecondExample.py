def find_an_element_in_a_sequence(item, targeted_sequence):
    def determine_sequence_type(sequence):
        if (type(sequence) == list):
            return "List"
        elif (type(sequence) == tuple):
            return "Tuple"

        else:
            return "String"

    sequence_type = determine_sequence_type(targeted_sequence)
    if item in targeted_sequence:
        print(f"Great news! {item} is in the {sequence_type}.")
    else:
        print(f"Bad news! {item} is in Not the {sequence_type}.")


# calling the function and passing the parameters
# Sequences
users_list = ["John", "Alice", "Bob", "William", "Elon", "Bill", "Sam", "Jeff", "Simran", "Adam", "Sara"]
users_tuple = ("John", "Alice", "Bob", "William", "Elon", "Bill", "Sam", "Jeff", "Simran", "Adam", "Sara")

find_an_element_in_a_sequence("William", users_list)
find_an_element_in_a_sequence("Cat", users_list)

find_an_element_in_a_sequence("William", users_tuple)
find_an_element_in_a_sequence("Cat", users_tuple)
