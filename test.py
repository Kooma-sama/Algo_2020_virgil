
# def print_comb() -> None:
#     for i in range(8):
#         for j in range(9):
#             for k in range(10):
#                 if i < j < k:
#                     print(f"{i}{j}{k}")

# #print_comb()




l2 = []

l = [1, 1, 1, 3, 2, 2, 3]
# count = 0
# for value in l:
#     if value == 1:
#         count = count + 1
#         if count == 1:
#             l2.append(value)
        
#     if value == 3:
#         count = count + 1
#         if count == 4:
#             l2.append(value)
        
#     if value == 2:
#         count = count + 1
#         if count == 5:
#             l2.append(value)

for value in l:
    if value not in l2:
        l2.append(value)
        
print(l2)
