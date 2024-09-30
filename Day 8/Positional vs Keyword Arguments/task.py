# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

def greet_with(name, location):
    print(f"How is the weather in {location}")
    print(f"Hello {name}")
    #print(f"How is the weather in {location}")

    print(f"Hello {name}, how is the weather in {location}?")


greet_with("Adrian","Houston")


greet_with(name="Adrian", location="Houston")
greet_with(location="Houston", name="Adrian")