nums = input("Enter integers separated by commas:").split(',')
result = []
for num in nums:
    n = int(num.strip())
    if n > 100:
        result.append('over')
    else:
        result.append(n)

print(result)