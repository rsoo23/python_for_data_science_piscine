# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rsoo <rsoo@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/18 10:10:16 by rsoo              #+#    #+#              #
#    Updated: 2023/09/18 10:28:53 by rsoo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# object: any 
# - this is to indicate that the param can accept any type of object

def all_thing_is_obj(object : any) -> int:
	if type(object) == list:
		print("List : " + str(type(object)))
	elif type(object) == tuple:
		print("Tuple : " + str(type(object)))
	elif type(object) == set:
		print("Set : " + str(type(object)))
	elif type(object) == dict:
		print("Dict : " + str(type(object)))
	elif type(object) == str:
		print(str(object) + " is in the kitchen : " + str(type(object)))
	else:
		print("Type not found")
	return (42)

