# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rsoo <rsoo@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/18 10:53:39 by rsoo              #+#    #+#              #
#    Updated: 2023/09/18 13:53:18 by rsoo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

# sys.argv[0] = filename

def main():
	num_args = len(sys.argv) - 1

	if num_args == 0:
		return

	assert num_args == 1, "more than one argument is provided"

	assert sys.argv[1].isdigit(), "arguments is not an integer"

	if int(sys.argv[1]) % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")
		
# entry point of script
# - if the script is running directly it will execute main(),
# otherwise if this file is imported as a module, it will not run
if __name__ == "__main__":
	main()
