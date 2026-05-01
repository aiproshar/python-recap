"""
Tow modules, time and datetime
Lets start with the time module
"""
import datetime
import hashlib
import string
import time

print(time.time()) # This prints number of seconds since epoch, epoch: January 1, 1970, 00:00:00 UTC (also called "Unix epoch" or "POSIX time")

'''
Lets generate 1 Million SHA-256 Hash and see how many seconds in take

'''
text = "Lets generate 5 Million SHA-256 Hash and see how many seconds in take. I bet this will not take a long time. Modern CPU has SHA instruction set, its super fast anyways"
# convert this to a byte stream
text = text.encode()
time_start = time.time()
for i in range(5000000):
    hashlib.sha256(text).hexdigest()

time_taken = time.time() - time_start
print(f"seconds took to generate 5 million SHA-256: {time_taken}")

# if we want to sleep for certain amount of time
print("Let's sleep for 500 ms")
time.sleep(0.500)
print("I am awake")

"""
The Datetime module
Datetime is package , datetime ois class
'from datetime import datetime' will eliminate the below weird syntax
"""
import datetime
print(datetime.datetime.now())  #prints local time, to TZ attached, TZ = timezone
print(datetime.datetime.now(tz=datetime.timezone.utc)) #timezone sensitive, this is based on UTC

#timedelta -> add a time to a datetime object
#imagine we want a cache to expire in 5 sec
current_time = datetime.datetime.now(tz=datetime.timezone.utc)
expire_time = current_time + datetime.timedelta(seconds=3)
print("Cache created with 3 sec lifetime")

while datetime.datetime.now(tz=datetime.timezone.utc) < expire_time:
    print("Cache is still valid")
    time.sleep(1)
print("Cache expired")

# How old you are exactly ? We can use datetime too
print("Enter Birth Year Month Date")
try:
    year = input()
    year = int(year)
    month = input()
    month = int(month)
    day = input()
    day = int(day)
    birth_time = datetime.datetime(year, month, day)
    current_time = datetime.datetime.now()
    age = current_time - birth_time
    print(f"Your current age :{age.days // 365} Years { (age.days % 365) // 30} Months")
except Exception as e:
    print(f"Exception occurred: {e.__class__.__name__}: {e}")