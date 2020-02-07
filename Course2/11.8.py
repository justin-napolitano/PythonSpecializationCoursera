11.8.py

#1 Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {}
for ch in placement:
    if ch not in d:
        d[ch] = 0
    d[ch] = d[ch] + 1

ks = d.keys()
min_value = list(ks)[0]
for k in ks:
    if d[k] < d[min_value]:
        min_value = k

#2 Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.
product = "iphone and android phones"

lett_d = {}
for ch in product:
    if ch not in lett_d:
        lett_d[ch] = 0
    lett_d[ch] = lett_d[ch] + 1

ks = lett_d.keys()
max_value = list(ks)[0]
for k in ks:
    if lett_d[k] > lett_d[max_value]:
        max_value = k
