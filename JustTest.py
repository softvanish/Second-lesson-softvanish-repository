
# # def disemvowel(string_):
# #     vowels = "aeiouAEIOU"
# #     lst = []
# #
# #     for i in string_:
# #         if i not in vowels:
# #             lst.append(i)
# #
# #     return "".join(lst)
# #
# # print(disemvowel("This website is for losers LOL!"))
#
# def unique_in_order(sequence):
#     result = []
#     sym = None
#     for i in sequence:
#         if i != sym:
#             result.append(i)
#             sym = i
#
#     return result
#
#
# print(unique_in_order('AAAABBBCCDAABBB'))

# a = (1, 2, [3, 6], 4, 5)
# a[2][0] = 0
# print(a)

def reverse_words(sentence):
    words = list[sentence]
    return words

print(reverse_words("i love music"))
