my_name = "Zed A. Shaw"
my_age = 35 # at time of writing?
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'School Bus Yellow'
my_hair = 'Brown'

print("Let's talk about %s." % my_name)
print("He's %s inches tall." % my_height)
print("He's %s pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# This line is a little tricky, try to get ti exactly right
print("If I had %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))