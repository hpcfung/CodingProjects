class Solution:
    def numSquares(self, n: int) -> int:
        from math import sqrt, floor, ceil

        record = [[n, floor(sqrt(n))]]
        for depth in range(1, 5):
            tmp_record = []
            for attempt in record:
                remainder, max_sq = attempt[0], attempt[1]
                ub = min(max_sq, floor(sqrt(remainder)))
                lb = ceil(sqrt(remainder/4))
                node = 0
                print(f"lb {lb}, ub {ub}, tot {ub-lb+1}")
                for k in range(ub, lb-1, -1):
                    node += 1
                    new_remainder = remainder - k*k
                    if new_remainder == 0:
                        print(f"node = {node}")
                        return depth
                    tmp_record.append([new_remainder, k])
                print(f"node = {node}")
            record = tmp_record        

mySol = Solution()
print(mySol.numSquares(1000))
