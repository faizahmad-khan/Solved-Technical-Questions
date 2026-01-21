# student = {
#     "name":["Alice", "Mohit", "Muskan"],
#     "age" :[20,19,25],
#     "Roll no":[101,102,103],
#     "city":["London", "Kanpur", "Lucknow"],
#     "Grade":["A", "B", "A+"]
# }
# print(student["name"].count("Alice"))
# print(student["name"])
#Count frequency of word in a sentence
# sentence = "My name is faiz and my friend name is faiz"
# words = sentence.split()
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# print(word_count)
#Count frequency of word in a sentence
student ={
    "word":"my name is faiz and my friend name is faiz"
}
print(student["word"].count("faiz"))

product ={
    "name":["laptop", "mouse", "keyboard", "monitor", "mouse"],
    "price":[50000, 1500, 2000, 10000, 1500]
   
}