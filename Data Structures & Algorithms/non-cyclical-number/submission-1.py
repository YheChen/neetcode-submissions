class Solution:
    def isHappy(self, n: int) -> bool:
        
        def replace(n: int) -> int:
            output = 0

            while n:
                digit = n % 10
                output += digit * digit
                n //= 10
            return output
            
        seen = set()

        while True:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n = replace(n)