# # x = -121
# # if x > 0:
# #     x = str(x)
# #     a = []
# #     for i in x:
# #         a.append(i)
# #     b = a[::-1]
# #     if a == b:
# #         print(True)
# # print(s)
# #     else:
# #         print(False)
# # else:
# #     print(False)
# #
# # nums = [1, 3, 5, 6]
# # target = 3
# # print(nums.index(target))
#
# # n = 199
# # summa = 0
# # summa2 = 0
# # summa3 = 0
# # for i in str(n):
# #     summa += int(i)
# # if len(str(summa)) > 1:
# #     for i in str(summa):
# #         summa2 += int(i)
# # else:
# #     print(summa)
# # if len(str(summa2)) > 1:
# #     for i in str(summa2):
# #         summa3 += int(i)
# #     print(summa3)
# # else:
# #     print(summa2)
#
#
# # nums = [5, 7, 7, 8, 8, 10]
# # nums2 = nums[::-1]
# # target = 8
# # a = []
# # a.append(nums.index(target))
# # a.append(len(nums) - nums2.index(target) -1)
# # print(a)
#
#
# # nums = [0, 4, 5, 3, 6]
# # nums1 = set(nums)
# # print(True) if len(nums) != len(nums1) else print(False)
#
# # a = 10
# # count = 0
# # for i in range(a):
# #     if i
# # print(count)
#
#
# # a = input()
# # b = input()
# #
# # al = []
# # for i in a:
# #     al.append(i)
# #
# # bl = []
# # for i in b:
# #     bl.append(i)
# #
# # bool = True
# #
# # if len(al) == len(bl):
# #     for i in al:
# #         if i in bl:
# #             bool = True
# #         else:
# #             bool = False
# #             break
# #
# #     print(bool)
# # else:
# #     print(False)
#
#
# class Shape:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#     def perimeter(self):
#         return 2 * (self.a + self.b)
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__(radius)
#         self.radius = radius
#
#
# # class Shape:
# #     def __init__(self, a, b):
# #         self.a = a
# #         self.b = b
# #
# #     def area(self):
# #         return self.a * self.b
# #
# #     def perimeter(self):
# #         return 2 * (self.a + self.b)
# #
# #
# # class Circle(Shape):
# #     def __init__(self, radius):
# #         super().__init__(radius)
# #         self.radius = radius
# #
# #     def area(self):
# #         return 3.14 * self.radius ** 2
# #
# #     def perimeter(self):
# #         return 2 * 3.14 * self.radius
# #
# #
# # class Rectangle(Shape):
# #     def __init__(self, a, b):
# #         super().__init__(a, b)
# #
# #
# # class Triangle(Shape):
# #     def __init__(self, base, height, side1, side2, side3):
# #         self.base = base
# #         self.height = height
# #         self.side1 = side1
# #         self.side2 = side2
# #         self.side3 = side3
# #
# #     def area(self):
# #         return 0.5 * self.base * self.height
# #
# #     def perimeter(self):
# #         return self.side1 + self.side2 + self.side3
# #
# #
# # c = Rectangle(5, 20)
# # print(c.perimeter())
# #
# #     def area(self):
# #         return 3.14 * self.radius ** 2
# #
# #     def perimeter(self):
# #         return 2 * 3.14 * self.radius
# #
# #
# # class Rectangle(Shape):
# #     def __init__(self, a, b):
# #         super().__init__(a, b)
# #
# #
# # class Triangle(Shape):
# #     def __init__(self, base, height, side1, side2, side3):
# #         self.base = base
# #         self.height = height
# #         self.side1 = side1
# #         self.side2 = side2
# #         self.side3 = side3
# #
# #     def area(self):
# #         return 0.5 * self.base * self.height
# #
# #     def perimeter(self):
# #         return self.side1 + self.side2 + self.side3
# #
# #
# # c = Circle(5)
# # s = Triangle(5, 8, 3, 4, 6)
# # print(s,c.perimeter())
# #
#
#
# # nums1 = [1, 2]
# # nums2 = [3, 4]
# # for i in nums2:
# #     nums1.append(i)
# #
# # lan = len(nums1)
# # if lan % 2 == 0:
# #     g = (nums1[lan // 2] + nums1[lan // 2 - 1]) / 2
# #     print(g)
# # else:
# #     h = nums1[lan // 2]
# #     print(h)
#
#
# #
# # from abc import ABC, abstractmethod
# #
# #
# # class Page(ABC):
# #     @abstractmethod
# #     def img(self):
# #         pass
# #
# #     @abstractmethod
# #     def title(self):
# #         pass
# #
# #     @abstractmethod
# #     def text(self):
# #         pass
# #
# #     @abstractmethod
# #     def input(self):
# #         pass
# #
# #     @abstractmethod
# #     def catigories(self):
# #         pass
# #
# #     @abstractmethod
# #     def recent(self):
# #         pass
# #
# # class Page1(Page):
# #     def __init__(self, namepage):
# #         self.namepage = namepage
# #
# #     def get_name(self):
# #         return self.namepage
# #
# #     def get_info(self):
# #         return f'{self.namepage}'
# #
# #     def get_price(self):
# #         return self.price
# #
# #     def set_price(self, x):
# #         self.price = x
# #
# #     def str(self):
# #         return self.name
#
#
# # lists = [[]]
# # l = []
# # for j in range(len(lists)):
# #     if len(lists) > 1:
# #         for i in lists[j]:
# #             l.append(i)
# # print(sorted(l))
#
# # class Contact:
# #     def __init__(self, name, email, subject, message):
# #         self.name = name
# #         self.email = email
# #         self.subject = subject
# #         self.message = message
# #
# #     def accept(self):
# #         return "Accepted!"
# #
# #
# # def con():
# #     name = input()
# #     email = input()
# #     subject = input()
# #     message = input()
# #     con = Contact(name, email, subject, message)
# #     return con
# #
# #
# # a = int(input())
# # for i in range(a):
# #     con()
# #     print(con.accept())
#
#
# # num1 = "123"
# # num2 = "456"
# # num1, num2 = int(num1), int(num2)
# # return num1 * num2
#
# # num1 = "11"
# # num2 = "123"
# # num1, num2 = int(num1), int(num2)
# # num1, num2 = max(num1, num2), min(num1, num2)
# # num1 = num1 + num2
# # return num1
#
#
# # s = "Hello World"
# # a = [i for i in s.split()]
# # print(len(a[-1]))
#
#
#
# import re
# s = "A man, a plan, a canal: Panama"
# s = re.sub(r'[^a-zA-Z0-9]', '', s)
# s = s.lower()
# rs = s[::-1]
# if s == rs:
#     print(True)
# else:
#     print(False)
#
# nums = [5, 4, -1, 7, 8]
# print(sum(nums))

#
# head = [1, 2, 3, 4, 5]
# # n = 2
# # a = head.pop(-n)
# del head[-n]
# print(head)
# print(head)


# nums = [5, 7, 7, 8, 8, 10]
# target = 6
# nums2 = nums[::-1]
# if target in nums:
#     print(nums.index(target))
#     print(len(nums) - nums2.index(target) - 1)
# else:
#
#   print(-1, -1)

# nums = [1, 2, 5, 2, 3]
# target = 2
# a = []
# nums = sorted(nums)
# for i in range(len(nums)):
#     if nums[i] == target:
#         a.append(i)
# print(a)

# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 0
#
# print(nums.index(target)) if target in nums else print(-1)

# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums2 = set(nums)
# a = len(nums) - len(nums2)
# print(a, nums[:a])
#
# s = "CIL"
# d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
# r = 0
# if (len(s) == 0):
#     print(0)
# for i in range(len(s) - 1):
#     if (d[s[i]] < d[s[i + 1]]):
#         r -= d[s[i]]
#     else:
#         r += d[s[i]]
# r += d[s[-1]]
# print(r)

# list1 = [1, 2, 4]
# list2 = [1, 3, 4]
# for i in list2:
#     list1.append(i)
# print(sorted(list1))

# haystack = "sadbutsad"
# needle = "sad"
# print(haystack.index(needle))

#
# nums = [1, 3, 5, 6]
# target = 2
# if target in nums:
#     print(nums.index(target))
# else:
#     nums.append(target)
#     nums = sorted(nums)
#     print(nums.index(target))

#
# l1 = [2, 4, 3]
# l2 = [5, 6, 4]
# a = []
# for i, j in l1, l2:
#     a.append(i + j)
# print(a)

# nums = [7, 8, 9, 11, 12]
# a = []
# for i in nums:
#     if i > 0:
#         a.append(i)
# a = sorted(a)
# b = [i for i in range(1, max(a) + 1)]
# for i in range(len(b) - 1):
#     if a[i] != b[i]:
#         print(b[i])
#         break

#
# board = [["a", "b"], ["c", "d"]]
# word = "abcd"
# a = []
# g = 0
# for i in board:
#     for j in i:
#         a.append(j)
# for h in word:
#     if h in a:
#         g += 1
#         a.remove(h)
# if g == len(word):
#     print(True)
# else:
#     print(False)
# print(a)

#
# s = "()[]{"
# a = False
# for i in range(len(s) // 2):
#     if s[i] == "(" and s[i + 1] == ")" or s[i] == "[" and s[i + 1] == "]" or s[i] == "{" and s[i + 1] == "}":
#         a = True
#     else:
#         a = False
# print(a)

# s = "{[]}"
# a = []
# for i in s:
#     a.append(i)
# if "(" in a and ")" in a:
#     a.remove("(")
#     a.remove(")")
# if "[" in a and "]" in a:
#     a.remove("[")
#     a.remove("]")
# if "{" in a and "}" in a:
#     a.remove("{")
#     a.remove("}")
# if len(a) == 0:
#     print(True)
# else:
#     print(False)

#
# a = ""
# strs = ["flower", "flow", "flight"]
#
#
# strs = ["flower","flow","flight"]
# prefix = strs[0][0]
# for i in range(len(strs)):
#     for j in range(len(prefix)):
#         if strs[i][j] != prefix[j]:
#             prefix.pop(prefix[j])
# print(prefix)

# a = ""
# b = ""
# strs = ["flower", "flow", "flight"]
# a += strs[0]
# strs.remove(strs[0])
# for i in strs:
#     for j in i:
#         if a[0] == j:
#             b += j
#
# print(b)


# head = [1, 2, 2, 1]
# a = head[::-1]
# print(True) if head == a else print(False)


# x = 120
# d = []
# ab = 0
# if x <= 0:
#     ab = 1
#     x = abs(x)
# x = str(x)
# for i in x:
#     d.append(int(i))
# d = d[::-1]
# h = ""
# if ab == 1:
#     h += "-"
# for j in d:
#     h += str(j)
# h = int(h)
# print(h, type(h))

# #
# nums = [3, 4, -1, 1]
# a = [i for i in nums if i > 0 and i < 100000]
# s = 1
# while s in a:
#     s += 1
# print(s)


# nums = [1, 2]
# nums = set(nums)
# if len(nums) >= 3:
#     print(nums)
#     for i in range(2):
#         nums.remove(max(nums))
#         print(nums)
#     print(max(nums))
# else:
#     print(max(nums))


# l1 = [7, 2, 4, 3]
# l2 = [5, 6, 4]
# a = ""
# b = ""
# for i in l1:
#     a += str(i)
# for j in l2:
#     b += str(j)
# a, b = int(a), int(b)
# a += b
# l1.clear()
# for i in str(a):
#     l1.append(int(i))
# print(l1)

# a = "Hello, my name is John"
# b = [i for i in a.split()]
# print(len(b))


# s = "()[]{}"
# s = s.replace('()', "").replace('[]', "").replace('{}', "")
# print(False) if len(s) != 0 else print(True)

# a = [i for i in range()]
# head = [1, 2, 3, 4, 5]

