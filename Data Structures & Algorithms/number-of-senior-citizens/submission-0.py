class Solution:
    def countSeniors(self, details: List[str]) -> int:
        old = 0
        for i in range(len(details)):
            age = details[i][-4] + details[i][-3]
            if int(age) > 60:
                old += 1
        return old
        