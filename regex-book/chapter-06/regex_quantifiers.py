import re

pattern1 = re.findall(r'x\s*y', 'xy')
pattern2 = re.findall(r'x\s+y', 'xy')
pattern3 = re.findall(r'x\s*y', 'x y')
pattern4 = re.findall(r'x\s+y', 'x y')

print('* will give the result as', pattern1)
print('+ will give the result as', pattern2)
print('* will give the result as', pattern3)
print('+ will give the result as', pattern4)
