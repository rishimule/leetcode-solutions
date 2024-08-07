class Solution:
    def numberToWords(self, num: int) -> str:
        place = {
            1000        : "Thousand",
            1000000     : "Million",
            1000000000  : "Billion",
        }

        tens = {
            20 : "Twenty",
            30 : "Thirty",
            40 : "Forty",
            50 : "Fifty", 
            60 : "Sixty", 
            70 : "Seventy",
            80 : "Eighty",
            90 : "Ninety"
        }
        
        units = {
            0 : "", 
            1 : "One",
            2 : "Two",
            3 : "Three",
            4 : "Four",
            5 : "Five",
            6 : "Six",
            7 : "Seven",
            8 : "Eight",
            9 : "Nine",
            10 : "Ten",
            11 : "Eleven",
            12 : "Twelve",
            13 : "Thirteen",
            14 : "Fourteen",
            15 : "Fifteen",
            16 : "Sixteen",
            17 : "Seventeen",
            18 : "Eighteen",
            19 : "Nineteen",
        }
        
        def twodigitconversion(n):
            ans = ""
            
            if n < 20:
                return units[n]
            else:
                d = n // 10
                ans += tens[d*10]
                d = n % 10
                ans += " " + units[d]
                return ans
                
        
        def threedigitconversion(n):
            ans = ""
            d = n // 100
            if d > 0:
               ans += units[d] + " Hundred"
            d = n % 100
            if d > 0:
                ans += " " + twodigitconversion(d)
            
            return ans.strip()
        
        # Check for zero
        if num == 0:
            return "Zero"
        
        divs = list(place.keys())
        divs.sort(reverse=True)
        
        res = ""
        
        for check in divs:
            if num == 0:
                break
            d = num // check
            if d > 0:
                res += threedigitconversion(d) + " " + place[check] + " "
                
            num = num % check
        
        if num > 0:
            res += threedigitconversion(num)
        
        return res.strip().replace("  "," ").replace("  "," ")



# s = Solution()
# s.numberToWords(num = 1234567) # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
