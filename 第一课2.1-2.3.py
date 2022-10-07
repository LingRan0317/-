#1_hellow world
print('hellow python world!')

#2修改字符串大小写
name="Xing YUe"
print(name.title())
print(name.upper())
print(name.lower())

#3合并字符串
first_name="Xing"
last_name="Yue"
full_name=first_name+" "+last_name
print(full_name)

message="Hi,"+full_name.title()+"!"
print(message)

#4制表符与换行符
print("Luaguages:\n\tPython\n\tC\n\tJava")

#删除空白
favorite_language="   python  "
favorite_language=favorite_language.rstrip().lstrip()
print(favorite_language)

