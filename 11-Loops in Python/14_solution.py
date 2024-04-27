s= "madamd"
reversed_str = ""
for ch in s:
    reversed_str = ch + reversed_str 

if(reversed_str == s):
    print("Palindrome")
else:
    print("Not Palindrom")