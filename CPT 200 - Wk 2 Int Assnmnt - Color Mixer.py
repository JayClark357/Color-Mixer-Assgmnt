# Lists with primary and secondary colors

p_list = ['Red', 'Blue', 'Yellow']
s_list = ['Purple', 'Orange', 'Green']

# User asked to enter colors from list choice values or given new 'error' prompt to retype
print("Let's make a new color from putting two other colors together.") 
p_color_1 = str(input("Please choose 1st primary color - Red, Blue, or Yellow:"))
if p_color_1 not in p_list:
     print('Please choose again')

p_color_2 = str(input("Please choose 2nd primary color - Red, Blue, or Yellow:"))
if p_color_2 not in p_list:
     print('Please choose again')

# Red/Blue color combination output

if p_color_1 == p_list[0] and p_color_2 == p_list[1] :
   print(s_list[0])
if p_color_1 == p_list[1] and p_color_2 == p_list[0] :
   print(s_list[0])

# Red/Yellow color combination output

if p_color_1 == p_list[0] and p_color_2 == p_list[2] :
   print(s_list[1])
if p_color_1 == p_list[2] and p_color_2 == p_list[0] :
   print(s_list[1])

# Blue/Yellow color combination output

if p_color_1 == p_list[1] and p_color_2 == p_list[2] :
   print(s_list[2])
if p_color_1 == p_list[2] and p_color_2 == p_list[1] :
   print(s_list[2])






    

