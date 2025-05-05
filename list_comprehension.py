num = [1,2,3,4,5,87,7]

new_list = [x**2 for x in num]
print(new_list)

name = 'gunjan'
new_list = [letter for letter in name if letter == 'n']
print(new_list)

student_list = ["kidda", "achintya", "kumar"]
new_dict = {student: 0 for student in student_list}
print(new_dict)

original_dict = {'kidda': 0, 'achintya': 0, 'kumar': 0}
change_dict = {key:val+1 for key,val in original_dict.items()}
print(change_dict)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
word_count = {word: len(word) for word in words}
print(word_count)
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {key:(val * 9/5) + 32 for key,val in weather_c.items()}
print(weather_f)
