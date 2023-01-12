i = int(input("Enter a num"))
rev = 0
x = i
while (i>0):
    rev = (rev*10)+(i%10)
    i = int(i//10)
if(x==rev):
    print("True")
else:
    print("False")


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x_str = str(x)
#         return x_str == x_str[::-1]
