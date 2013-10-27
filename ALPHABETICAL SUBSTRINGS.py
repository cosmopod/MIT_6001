# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print "Longest substring in alphabetical order is: beggh"

#In the case of ties, print the first substring.
#For example, if s = 'abcbcd', then your program should print "Longest substring in alphabetical order is: abc"


from itertools import count

s = "jdisjsd sdpkds sdpsdsdfposodksdpfok "

maxSubstr = s[0:0]
for start in range(len(s)):
    for end in count(start + len(maxSubstr) + 1):
        substr = s[start:end]
        if len(substr) != (end - start):
            break
        if sorted(substr) == list(substr):
            maxSubstr = substr

print "Longest substring in alphabetical order is: " + str(maxSubstr)
