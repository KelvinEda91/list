def amount_sum():
    money_list = [2, 5, 8, 2, 9, 5, 3, 7, 8, 1, 2, 5, 9, 2, 4, 2]
    print(money_list)
    my_set = set(money_list)  # Convert list to set to remove duplicates
    print(f"{sorted(my_set)} sorted figures")
    total_amount = sum(my_set)  # Compute the sum of the remaining numbers
    print(f"{total_amount} the sum result")

amount_sum() # Call the function to execute the codeh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               1