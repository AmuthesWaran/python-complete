test_list = ['sapple', 'orange', 'smango', 'grape']

start_letter = 's'


with_s = list(filter(lambda x: x.startswith(start_letter), test_list))
without_s = list(filter(lambda x: not x.startswith(start_letter), test_list))

print(with_s)
print(without_s)
