import yaml

# with open('./haha.yaml') as f:
#     a = yaml.safe_load(f)
# print(a)
repr()

a = {"haha": '1', "yoyo": '222'}

# print(type(a.keys()))
# print(a.keys())
# print(a.values())
# print(a.items())
# for c, d in a.items():
#     print(c)
#     print(d)
#     print('-----------')
str1 = '${haha}fasdfasf${yoyo}'
for key, value in a.items():
    str1 = str1.replace(f'${{{key}}}', value)
print(str1)

haha = 123
ee = '${{{}}}'.format(haha)
print(ee)