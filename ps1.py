#! /usr/bin/python3.6

# Take bit string as input from user
s = input()

# variable to keep the count of '1' encountered
c = 0

# Loop to find c 
for i in range(len(s)):
    if(s[i] == '1'):
        c += 1

# Appending approriate parity bit
if(c%2 == 0):
    s_pc = s + '1'
else:
    s_pc = s + '0'

# List to store the index where '0' is to be stuffed
idx = []
i = 0
while(i < len(s)):
    if(s[i:i+3] == '010'):  # Find '010' 
        i += 3
        idx.append(i)
    else:
        i += 1

# List containing original string and parity bit
s_pc_s = list(s_pc)

for i in range(len(idx)):
    s_pc_s.insert(idx[i]+i,'0')

# Original string along with stuffed '0' bits and parity bits
s_pc_s = "".join(s_pc_s)

# Append '0101' to denote end of string
s_f = s_pc_s + '0101'

# Print original string with parity
print(s_pc)

# print final string
print(s_f)


