# Program to calculate wheat on a chessboard

# Given the number of squares on a chessboard
num_of_squares = 64

# Calculates how many grains the ruler owed the inventor
for square in range(1, num_of_squares  + 1):
    grains_on_square = 2 ** (square - 1)

# Creating variables
# Area is in km ** 2 
wheat_weight = (grains_on_square * 50) / 1000000
"""This converts the wheat wheat in mg to kg"""
oregon_area = 254806
# Grain density was found on Google. 790kg/m ** 3 
grain_density = 790

# To calculate the depth we need the volume of the wheat grains
volume = wheat_weight / grain_density

# Depth is d = volume/surface area
depth = volume / oregon_area

print(f"Total grains of wheat: {grains_on_square}")
print(f"Total weight of wheat: {wheat_weight} kg")
print(f"The state of Oregon would be covered in: {depth} km of wheat!")    