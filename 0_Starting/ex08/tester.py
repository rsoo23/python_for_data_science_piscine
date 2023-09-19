
from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(260)):
    sleep(0.02)
print()
for elem in tqdm(range(260)):
    sleep(0.02)
print()
