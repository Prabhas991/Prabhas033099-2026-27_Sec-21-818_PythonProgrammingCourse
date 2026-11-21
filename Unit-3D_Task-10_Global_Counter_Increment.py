count = 0

def increment():
    global count
    count += 1
    print("Counter inside function:", count)

increment()
increment()
increment()

print("Final counter:", count)