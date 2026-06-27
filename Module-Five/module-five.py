# this functional approach uses other higher-order functions to filter and map the existing list to the returned list with the required values.
# it also uses lambda within higher-order functions to utilize first-class functions.
# combined, these functional paradigm features create a concise solution that emphasizes the transformation of data through function composition, rather than explicit control flow.
# also, the single return statement allows for the output data to be transformed without additional variable assignment, which embraces the avoidance of stateful operations and mutable data structures.

def functional_numbers(values):
	return list(map(lambda number: number ** 2, filter(lambda number: number % 2 != 0, values)))

# in contrast to the functional approach, this imperative function uses explicit loops and conditional statements to control the flow of exectution and state of the data.
# it iterates through the input list, checks if each number is odd, and if so, computes its square and appends it to a result list. 
# this step-by-step process and mutable variable assignment is characteristic of the imperative programming paradigm

def imperative_numbers(values):
	# mutable data structure to hold results
	result = []
	
    # explicit control flow to iterate the input data
	for number in values:
		
        # coditional statement to check if the number is odd for each element in the input list
		if number % 2 != 0:
			
            # mutate the data structure by appending the squared value of the odd number to the result list
			result.append(number ** 2)
			
	return result

# the object-oriented approach creates a model of a processor which performs the necessary storage and functional operations.
# it encapsulates the data (the list of values) within a member variable and the behavior (the processing function) within a member method.
# this function overrides the __str__ method in order to eliminate the need to externally call the processing function.
# this embraces the object-oriented paradigm's emphasis on encapsulation and abstraction, allowing the internal workings of the class to be hidden from the user while still providing a clear interface for interaction.
class NumberProcessor:

    # constructor to initialize the object with the input values
    def __init__(self, values):
        self.values = values

    # internal method for processing the internally stored data
    def process_numbers(self):
        result = []

        # similar control flow to the imperative approach, but encapsulated within a class method
        for value in self.values:
            if value % 2 != 0:
                result.append(value ** 2)

        return result
    
    # override the __str__ method to provide a clean public interface for interacting with the object, which reinforces abstraction by hiding the internal processing implementation
    def __str__(self):
        return f"Object-oriented approach's results: {self.process_numbers()}"


if __name__ == "__main__":
	values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	print(f"Functional approach's results: {functional_numbers(values)}")
	print(f"Imperative approach's results: {imperative_numbers(values)}")
	print(NumberProcessor(values))

