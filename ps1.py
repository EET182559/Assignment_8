#! /usr/bin/python3.6

s = input()

c = 0

for i in range(len(s)):
    if(s[i] == 1):
        c += 1

if(c%2) == 0:
    s_pc = s + '1'
else:
    s_pc = s + '0'

idx = []
i = 0
while(i < len(s)):
    if(s[i:i+3] == '010'):
        i += 3
        idx.append(i)
    else:
        i += 1

s_pc_s = list(s_pc)

for i in range(len(idx)):
    s_pc_s.insert(idx[i]+i,'0')

s_pc_s = "".join(s_pc_s)

s_f = s_pc_s + '0101'

print(s_pc)
print(s_f)


