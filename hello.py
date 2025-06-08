# ...existing code...
# Print a greeting to the console
print("Hello, World!")

# Print an informational message
print("This is a Python script.")

# Define a Greeter class
class Greeter:
    def __init__(self, name):
        # Initialize the Greeter with a name
        self.name = name
    def say_hello(self):
        return f"Hello, {self.name}!"

# Create and use the class
greeter = Greeter("User")
print(greeter.say_hello())