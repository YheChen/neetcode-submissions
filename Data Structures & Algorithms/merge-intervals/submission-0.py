class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = []
        curr_start, curr_end = intervals[0]

        for start, end in intervals[1:]:
            if start > curr_end:
                output.append([curr_start, curr_end])
                curr_start, curr_end = start, end
            else:
                curr_end = max(curr_end, end)

        output.append([curr_start, curr_end])

        return output