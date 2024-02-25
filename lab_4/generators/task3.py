def divisible_by_3_and_4(n):
    for x in range(n + 1):
        if x % 3 == 0 and x % 4 == 0:
            yield x


for x in divisible_by_3_and_4(int(input())):
    print(x, end=" ")


#######Alternative
# def divisible_by_3_and_4(num):
#     x = 0
#     while x <= num:
#         yield x
#         x += 12

# a = divisible_by_3_and_4(int(input()))

# for i in a:
#     print(i)
