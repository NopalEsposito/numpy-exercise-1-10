import numpy as np

# 1. Define the array
array_float = np.array([1.34, 5.4, 8.87, 4.53, 9.4])

# 2. Print the original array
print("Original:", array_float)

# 3. Print the rounded version
# This rounds to the nearest whole number (as a float)
print("Rounded: ", np.round(array_float))

#4. 
print("sqrt:", np.sqrt(array_float))

#radius of circle
radius_circle = array_float * np.pi * 2
print(radius_circle)




################################################################################################################################################################




#1. Generate 6x6 array for random int
#2.  Crop the image: extract only the "center" 4 x 4 pixels (removing the outermost top, bottom, left, and right border rows/columns).
#3. Count how many pixels in that $4 \times 4$ center are "bright" (value $> 150$).

rng = np.random.default_rng()

grayscale_image = rng.integers(1, 255, size=(6, 6))
image_crop = grayscale_image[1:-1, 1:-1]
bright_image = image_crop [ image_crop > 150]

print(image_crop)
print(np.sum(bright_image))



################################################################################################################################################################


student_numbers = rng.integers(0, 100, size=10)
pass_count = np.sum(student_numbers >= 60) # Counts the True values
student_status = np.where(student_numbers >= 60, "PASS", "FAIL")

print(student_numbers)
print(student_status)



################################################################################################################################################################


shopping_cart = rng.integers(5, 50, size=(3, 4))
shopping_cart_total_axis1 = np.sum(shopping_cart, axis=1) #calculate the shopping cart
shopping_cart_total = np.argmax(shopping_cart)

print(shopping_cart)
print(shopping_cart_total_axis1)
print(shopping_cart_total)




################################################################################################################################################################



#variable list
data_reshaper = rng.uniform(20, 35, size=(3, 4))
data_reshaper_tranpose = np.transpose(data_reshaper)
average_data_reshaper = np.mean(data_reshaper_tranpose, axis=1)

#execute
print(data_reshaper)
print(data_reshaper_tranpose)
print(average_data_reshaper)



################################################################################################################################################################

original_data = rng.integers(50, 100, size=10 )
original_data_mean = np.mean(original_data)
original_data_standard_deviation = np.std(original_data)

# The Parentheses make the difference!
standardized = (original_data - original_data_mean) / original_data_standard_deviation

# Verification:
print(np.mean(standardized)) # This should be a tiny number close to 0
print(standardized)


################################################################################################################################################################

grade = rng.uniform(60, 100, size=1)
grade_ceiling = np.ceil(grade)
grade_bonus = grade_ceiling - grade

print(grade)
print(grade_ceiling)
print(grade_bonus)