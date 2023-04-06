import wikipedia

wikipedia.set_lang('uz')

a = input("So'zni kiriting:")

print(wikipedia.search(a))
print(wikipedia.summary(a))