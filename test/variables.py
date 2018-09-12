userAge, userName = 30, 'Peter'
print(userAge)
print(userName)
print(str(userAge) + userName)

message = 'The price of this {} laptop is {} USD and the exchange rate is {} USD to 1 EUR'\
    .format('Apple', 1299, 1.235235245)

message = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'\
    .format('Apple', 1299, 1.235235245)

print(message)

message1 = '{0} is easier than {1}'.format('Python', 'Java')
print(message1)
