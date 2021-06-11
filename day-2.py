fname = 'Gaurav'
lname = 'Keshri'
age = '29'
status = True

print(f'''My name is {fname} {lname}.
I am {age} years old.
{status}''')

sentence = ('''My name is {} {}.
I am {} years old
{}.''').format(fname, lname, age, status)
print(sentence)
