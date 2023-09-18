# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rsoo <rsoo@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/18 10:32:16 by rsoo              #+#    #+#              #
#    Updated: 2023/09/18 10:48:15 by rsoo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# cannot do this: (if type(object) == NoneType:)

def NULL_not_found(object : any) -> int:
	if object is None:
		print("Nothing: " + str(object) + " " + str(type(object)))
	elif type(object) == float:
		print("Cheese: " + str(object) + " " + str(type(object)))
	elif type(object) == int:
		print("Zero: " + str(object) + " " + str(type(object)))
	elif type(object) == str and len(object) == 0:
		print("Empty: " + str(object) + " " + str(type(object)))
	elif type(object) == bool:
		print("Fake: " + str(object) + " " + str(type(object)))
	else:
		print("Type not found")
		return 1;
	return 0;
		
		
	
