name = "Mayur"
age = 43


message = "Hello {} ({})".format(name, age)

#order can be changed in below line by adding numbers in the bracket
message_num = "Hello {1} ({0})".format(name, age)

#You can define names in the brackets this is called Keyword arguments KWARGS
message_kwerg = "Hello {name} ({age})".format(name=name, age=age)


print(message)
print(message_num)
print(message_kwerg)