"""Split string and convert in Interger"""
time=input("Enter time:").split(':')
hour=int(time[0])
minutes=int(time[1])

print("hour:%i and minutes:%i"%(hour,minutes))