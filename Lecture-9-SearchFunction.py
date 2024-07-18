def find_an_element_in_a_sequence(item, targeted_sequence):
    if item in targeted_sequence:
        print(f"Great news! {item} is in the data!")
    else:
        print(f"Bad news! {item} is in NOT in the data!")


# calling the function and passing the parameters
users_list = ["John", "Alice", "Bob", "William", "Elon", "Bill", "Sam", "Jeff", "Simran", "Adam", "Sara"]

find_an_element_in_a_sequence("William", users_list)
find_an_element_in_a_sequence("Cat", users_list)

users_tuple = ("John", "Alice", "Bob", "William", "Elon", "Bill", "Sam", "Jeff", "Simran", "Adam", "Sara")
find_an_element_in_a_sequence("William", users_tuple)
find_an_element_in_a_sequence("Cat", users_tuple)
# Now I want to generarlize it so it works for both tuple and list!
