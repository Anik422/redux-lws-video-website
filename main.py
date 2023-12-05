class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num_list = ['999', '888', '777', '666', '555', '444', '333', '222', '111', '000']
        max_num = 0
        find = False
        for i in num_list:
            if i in num:
                if max_num < int(i):
                    find = True
                    max_num = int(i[0])
        if find:
            print(num_list[max_num])    
        else:
            print("") 


if __name__ == '__main__':
    Solution().largestGoodInteger("42352338")