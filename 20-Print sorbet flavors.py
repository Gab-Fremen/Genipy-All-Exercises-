"""
You're working for a restaurant and they're asking you to generate the sorbet menu.

Provide a script printing every possible sorbet duos from a given list of flavors.

Don't print recipes with twice the same flavor (no "Chocolate, Chocolate"), and don't print twice the same recipe (if you print "Vanilla, Chocolate", don't print "Chocolate, Vanilla", or vice-versa).

"""

FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]



#define a function to combine the flavors, it should take no parameters, and print every possible sorbet duos without repeating the same flavor or the same recipe
def combine_flavors():

    #define a variable to store the flavors that have already been used in the recipes, and set it to an empty list
    FLAVORS_GONE = [" "]
    
    #Use a nested for loop to go through the flavors in the FLAVORS list, and for each flavor, go through the flavors again to find the combinations
    for flavor1 in FLAVORS:
        
        for flavor2 in FLAVORS:

            #Use an if statement to check if the two flavors are not the same, and if the second flavor is not already in the FLAVORS_GONE list
            if flavor1 != flavor2:
                if flavor2 not in FLAVORS_GONE:
                    print(f"{flavor1}, {flavor2}")

        #After the inner loop, add the first flavor to the FLAVORS_GONE list to avoid repeating the same recipe
        FLAVORS_GONE.append(flavor1)
                
#call the function to print the combinations of flavors to the console
combine_flavors()