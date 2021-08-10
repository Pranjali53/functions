def Max_marks():
    B_list = 0
    while B_list < len(marks):
        Max=0
        S_list = 0
        while S_list < len(marks[B_list]):
            if marks[B_list][S_list]>Max:
                Max=marks[B_list][S_list]
            S_list = S_list + 1
        B_list = B_list + 1
        print (Max)
marks = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
Max_marks()


# def Max():
#     c1 = 0
#     while c1 < len(marks):
#         c2 = 0
#         Max=0
#         while c2 < len(marks[c1]):
#             if marks[c1][c2]>Max:
#                 Max=marks[c1][c2]
#             c2 = c2 + 1
#         c1 = c1 + 1
#         print(Max)
# marks = [[45, 21, 42, 63], [12, 42, 70, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
# Max()
