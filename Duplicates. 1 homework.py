#       HOMEWORK 1, DUPLICATES
# nums = [1, 5, 2, 1, 2, 4, 5, 1]
# converted_list = set()
# duplicate = {i for i in nums
#              if i in converted_list or (converted_list.add(i) or False)}
# print(duplicate)
class Duplicate(): #stexcenq class Duplicate anunov
    def dup(self, list_nums, list_dup): #stexcenq funcia, vorin tanq argument
        for i in range(len(list_nums)): #ancnenq list_nums-i vrayov, indexavorenq
            j = i+1
            if list_nums[i] == list_nums[j]:
                list_dup.add(list_nums[i])
                return list_dup
list_nums = [1, 5, 2, 1, 2, 4, 5, 1]
list_dup = list()
obj = Duplicate()
print(obj.dup(list_dup))