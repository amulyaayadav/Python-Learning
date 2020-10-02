name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word == 'From':
            hour = words[5].split(":")
            counts[hour[0]]=counts.get(hour[0],0)+1
        

for k,v in sorted(counts.items()):
	print(k,v)