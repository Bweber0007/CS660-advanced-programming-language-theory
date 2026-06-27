import json

# function to open and read the JSON file
def openFile(filename):
    try:
        with open(filename, 'r') as file:
            catalog = json.load(file)
        return catalog
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file {filename}.")
        return None

# recursively validate the input data structure
def recursive_input_validate(data):
    try:
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str):
                    raise TypeError("Keys must be strings.")

                recursive_input_validate(value)

        elif isinstance(data, list):
            for item in data:
                recursive_input_validate(item)

        elif not isinstance(data, (str, int, float, bool, type(None))):
            raise TypeError(f"Invalid value type: {type(data)}")

        return True

    except TypeError as e:
        print("Type error:", e)
        return False
    
# recursively traverse the nested structure and retrieve all object names
def recursive_nested_structure(data):
    try:
        names = []

        # check if the current data is a dictionary and look for keys containing "name"
        if isinstance(data, dict):
            for key, value in data.items():
                if "name" in key:
                    names.append(value)

                names.extend(recursive_nested_structure(value))

        elif isinstance(data, list):
            for item in data:
                names.extend(recursive_nested_structure(item))

        return names

    except TypeError as e:
        print("Type error:", e)
        return []

    except ValueError as e:
        print("Value error:", e)
        return []

    except RecursionError:
        print("Recursion error: Nested structure is too deep.")
        return []

# retrieve the deepest named leaf objects in the nested structure
def recursive_deepest_leaf(data):
    try:
        leaf_objects = []

        if isinstance(data, dict):
            current_object = {}
            has_deeper_object = False

            for key, value in data.items():

                # check if current object has a deeper named leaf
                if isinstance(value, dict):
                    if any("name" in item for item in value.keys()):
                        has_deeper_object = True
                        leaf_objects.extend(recursive_deepest_leaf(value))

                elif isinstance(value, list):
                    if any(isinstance(item, (dict, list)) for item in value):
                        has_deeper_object = True
                        leaf_objects.extend(recursive_deepest_leaf(value))
                    else:
                        current_object[key] = value

                else:
                    current_object[key] = value

            if not has_deeper_object and current_object:
                leaf_objects.append(current_object)

        elif isinstance(data, list):
            for item in data:
                leaf_objects.extend(recursive_deepest_leaf(item))

        return leaf_objects

    except (TypeError, ValueError) as e:
        print("Error:", e)
        return []

# custom function that takes another function as a parameter to format galaxy distances
def format_galaxy_distances(galaxy_list, function):
    try:
        return {
            galaxy["name"]: function(galaxy["distance_ly"])
            for galaxy in galaxy_list
        }

    except (TypeError, KeyError) as e:
        print("Formatting error:", e)
        return {}
    
if __name__ == "__main__":

    filename = "catalog.json"
    catalog = openFile(filename)

    if catalog is not None:

        print(f"\nInput Validation:\n{recursive_input_validate(catalog)}\n")
        nested_structure = recursive_nested_structure(catalog)

        print(f"Object Names:\n{nested_structure}\n")
        deepest_leaf = recursive_deepest_leaf(catalog)

        print("Deepest Leaves:")
        for leaf in deepest_leaf:
            print(leaf) 
        
        galaxies = catalog["astronomical_catalog"]["galaxies"]

        # anonymous function to convert light years to million light years and format the output
        print("\nGalaxies with Distance in Million Light Years:")
        print(list(map(lambda galaxy: f"{galaxy['name']}: {round(galaxy['distance_ly'] / 1000000, 2)} million light years", galaxies)))

        # higher order function to filter galaxies by type
        print("\nSpiral Galaxies:")
        print(list(filter(lambda galaxy: galaxy["type"] == "spiral", galaxies)))

        # call custom function and pass a lambda function as the function parameter
        print("\nCustom Light Years Format:")
        distances_thousands = format_galaxy_distances(catalog["astronomical_catalog"]["galaxies"],lambda distance: f"{round(distance / 1000, 2)} thousand light years")
        print(distances_thousands)

