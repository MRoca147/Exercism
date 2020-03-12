class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ","")

    def valid(self):
        string = self.card_num[::-1]

        for num in string:
            if not num.isdigit():
                return False

        nums = [int(num) for num in string]

        if len(nums) < 2:
            return False

        for i in range(1, len(nums), 2):
            number = nums[i] * 2
            if number > 9:
                number -= 9
            nums[i] = number

        if sum(nums) % 10 == 0:
            return True
        else:
            return False
