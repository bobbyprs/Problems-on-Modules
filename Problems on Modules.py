import urllib.request 
import re 

url = urllib.request.urlopen ('https://media.geeksforgeeks.org/wp-content/uploads/e-mail-1.txt') 
for line in url: 
	s = line.decode().strip() 
	reg = re.findall(r"[A-Za-z0-9._%+-]+"
					r"@[A-Za-z0-9.-]+"
					r"\.[A-Za-z]{2,4}", s) 
	print(reg) 
###################################################
queue = []

queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)


print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

