nums = input("Enter inegers separated by commas :").split(',')
result = [int(num.strip()) for num in nums if int(num.strip())%2 !=0]
print (result)