import itertools

count = 0
# vars = [True, False]
# for K in vars:
#     for L in vars:
#         for M in vars:
#             for N in vars:
#                 count += not(not(K or L) or (L and M and N)) 

# print(count)

B = (True, False)
for K, L, M, N in itertools.product(B, B, B, B):
    count += not(not(K or L) or (L and M and N)) 

print(count)