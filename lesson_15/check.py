# import string
#
# emails = ['fgg.g@gmail.com', 'dd..h@mm.com']
# email = emails[0]
# letters = string.ascii_lowercase
# digits = string.digits
# symbols = '_-.'
# marker = True
#
#
# def check(email):
#     marker = True
#     if email.count('@ ') == 1:
#
#         left, right = email.split('@')
#         if right.count('.') == 1:
#             r_1, r_2 = right.split('.')
#             marker = all([letter in letters for letter in r_1]) and \
#                      all([letter in letters for letter in r_2]) and \
#                      2 < len(r_2) < 4
#         if all([(letter in letters + digits + symbols) for letter in left]):
#             if left[0] in letters and left[-1] in letters:
#                 l = letters[1:-1]
#                 for i in range(len(l)):
#                     if l[i - 1] in symbols and l[i] in symbols:
#                         marker = False
#                     else:
#                         marker = True
#     else:
#         marker = False
#     return marker
#
#
# for email in emails:
#     print(check(email))
import itertools

m = list(itertools.product(range(1, 9), 'ABCDEFGH'))
print(m)
