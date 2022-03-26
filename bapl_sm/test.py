file=open('file3.sp','r')
lines=file.readlines()

print(type(lines))

idx=lines.index("v2 cwl<0> 0 DC=1.2")
print(idx)

indices = [i for i, s in enumerate(lines) if "v2 cwl<0> 0 DC=1.2" in s]

print(indices)
# print(lines)
# for line in lines:
#     if "cwl<0> 0 DC" in line:
#         print(line)