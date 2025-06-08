# ...existing code...
print ("Hello, World!")

print ("This is a Python script.")

class Greeter:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        return f"Hello, {self.name}!"

# Create and use the class
greeter = Greeter("User")
print(greeter.say_hello())