#          HOMEWORK 2,   TWO SUM
#trvac e list` nums, ev amboxj tiv` target, betq e tpenq list-i ayn elementneri indexner@, voronc gumar@ target e
class TwoSum: #stexcum enq class TwoSum anunov
    def two_sum(self, nums, target): #stexcenq def funkcia, vorin talis enq argumentner` nums, target
        for i in range(len(nums)): #hertov ancnum enq nums-i erkarutyan vrayov, indeqsavorum enq (i-n indeqsn e)
            for j in range(i+1, len(nums)):#j-ov nshanakum enq (i+1) index@
                if nums[i] + nums[j] == target: #ete i ev j indexneri tveri gumar@ == e target, apa return anenq [i, j] zuyg@
                    return [i, j]
# nums = input()#ays depqum pordzel em inputov ashxatacnel,
                     #bayc tvacs bolor arjeqneri nepqum None e veradardznum, amenayn havanakanutyamb voreve bactoxum unem
# target = input()
# first_exc = TwoSum()
# print(first_exc.two_sum(nums, target))
nums = [2, 5, 3, 7, 3, 8]
exc_1 = TwoSum()
print(exc_1.two_sum(nums, 12))

