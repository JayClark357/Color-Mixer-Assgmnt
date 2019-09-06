# List with primary and secondary colors
p_list = ['Red', 'Blue', 'Yellow']
s_list = ['Purple', 'Orange', 'Green']

# User asked to enter primary color list value
p_color_1 = input(str("Please choose first primary color - Red, Blue, or Yellow:"))
if p_color_1 not in p_list:
     print('Please choose again')
p_color_2 = input(str("Please choose second primary color - Red, Blue, or Yellow:"))
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

# Incorrect user input - error prompts
if p_color_1 not in p_list :
    print('Please choose your 1st color from the list')
if p_color_2 not in p_list:
    print('Please choose your 2nd color from the list')
if s_list != True:
    p_color_1 = input(str("Please choose first primary color - Red, Blue, or Yellow:"))

    p_color_2 = input(str("Please choose second primary color - Red, Blue, or Yellow:"))
while p_color_1 == p_color_2 :
    p_color_1 = input(str("Please choose first primary color - Red, Blue, or Yellow:"))

    p_color_2 = input(str("Please choose second primary color - Red, Blue, or Yellow:"))




    

