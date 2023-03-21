#           HOMEWORK 3, GCD
def GCDproject(nums): #stexcenq function, vorin haxordelu enq tveri sharq, list
    small = min(nums) #gtnenq listi amenapoqr masnik@
    # for j in range(nums): # hajord ereq toxov pordzel em bacarel 0-n, bayc chem karoxacel
    #     if nums[j] == 0:
    #         return None
    for i in range(1, small+1): #ancnenq 1 -ic minchev amenapoqr+1 tveri vrayov, (vor amenapoqr tiv@ bac chtoxnenq, dra hamar +1)
        if((nums[0] % i == 0) and (nums[1] % i == 0) and (nums[2] % i == 0)): #ete if-i tak exac payman@ bavararum e
            gcd = i # uremn gsd-n henc ayd i-n e
    return gcd
nums = [24, 36, 16] # urish tver texadrelu depqum cragir@ karces te ashxatum e normal
print(GCDproject(nums))