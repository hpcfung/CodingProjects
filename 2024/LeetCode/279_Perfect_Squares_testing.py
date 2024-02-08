from matplotlib import pyplot as plt

class Solution:
    def numSquares(self, n: int) -> int:
        from math import sqrt, floor, ceil

        self.count = 0
        record = [[n, floor(sqrt(n))]]
        for depth in range(1, 5):
            remaining_depth = 4 - depth + 1
            tmp_record = []
            for attempt in record:
                remainder, max_sq = attempt[0], attempt[1]
                ub = min(max_sq, floor(sqrt(remainder)))
                lb = ceil(sqrt(remainder / remaining_depth))
                for k in range(ub, lb - 1, -1):
                    new_remainder = remainder - k * k
                    self.count += 1
                    # print(self.count, remainder, k, new_remainder)
                    if new_remainder == 0:
                        return depth
                    tmp_record.append([new_remainder, k])
            record = tmp_record


if __name__ == '__main__':
    max_n = 5000

    all_counts = []
    all_avgs = []
    mySol = Solution()
    _sum = 0
    for k in range(1, max_n+1):
        mySol.numSquares(k)
        all_counts.append(mySol.count)
        _sum += mySol.count
        avg = _sum / k
        all_avgs.append(avg)
        print(k, mySol.count, avg)
    plt.plot(range(1, max_n+1), all_counts)
    plt.plot(range(1, max_n+1), all_avgs)
    plt.show()
