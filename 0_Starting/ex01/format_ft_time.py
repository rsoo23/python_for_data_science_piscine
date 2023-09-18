# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rsoo <rsoo@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/18 09:23:16 by rsoo              #+#    #+#              #
#    Updated: 2023/09/18 10:09:15 by rsoo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import datetime

current_time = time.time()
# two ways you can format the time:
formatted_current_time = f"{current_time:,.4f}"
current_time_scientific = "{:.2e}".format(current_time)

current_datetime = datetime.datetime.now()
formatted_current_datetime = current_datetime.strftime("%B %d %Y")

past_datetime = datetime.datetime(1970, 1, 1)
formatted_past_datetime = past_datetime.strftime("%B %d, %Y")

print(f"Seconds since {formatted_past_datetime}: {formatted_current_time} or {current_time_scientific} in scientific notation")
print(f"{formatted_current_datetime}")

# Expected output:
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$
