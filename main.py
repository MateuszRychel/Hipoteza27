class Program:
    def find_power(self, x):
        num = x
        temp = 0
        power = 0
        while num > 0:
            temp = num % 10
            num = num // 10
            power = power + 1
        return power

    def check_if_numbers_are_equal(self, x):
        power = self.find_power(x)
        num = x
        sum = 0

        while num > 0:
            temp = num % 10
            sum += (temp ** power)
            num = num // 10

        return sum == x

Test = Program()
print(Test.check_if_numbers_are_equal(371))
