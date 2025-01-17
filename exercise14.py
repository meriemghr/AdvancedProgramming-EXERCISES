word = input("Enter a string: ")
frame_width = 30
border = '*' * frame_width
spaces = (frame_width - len(word)) // 2

middle_line = '*' * spaces + word + '*' * (frame_width - len(word) - spaces)

print(border)
print(middle_line)
print(border)
