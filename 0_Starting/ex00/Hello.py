# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rsoo <rsoo@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/18 09:23:19 by rsoo              #+#    #+#              #
#    Updated: 2023/09/18 09:23:22 by rsoo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# List
ft_list[1] = "World"

# Tuple
temp_list = list(ft_tuple)
temp_list[1] = "Malaysia"
ft_tuple = tuple(temp_list)

# Set
ft_set.remove("tutu!")
ft_set.add("Kuala Lumpur")

# Dictionary
ft_dict["Hello"] = "42 Kuala Lumpur"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# List
# - collection of ordered and mutable elements
# - you can add, remove, modify elements

# Tuple
# - collection of ordered and immutable elements
# - you cannot change the elements

# Set
# - unordered collection of unique elements
# - do not allow duplicate values
# - if you add the same element > 1, it will only appear once

# Dictionary
# - collection of key value pairs, where each key is unique
# - you can access values by their keys, making it efficient for looking up data by a specific identifier

# *Ordered - same order as the data is initialised
# *Unordered - order is always different and is not meaningful 