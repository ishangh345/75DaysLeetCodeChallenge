class Solution:
    def largestRectangleArea(self, heights):

        stack = []
        max_area = 0

        # Add extra 0 height to flush stack
        heights.append(0)

        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:

                height = heights[stack.pop()]

                # Width calculation
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = height * width
                max_area = max(max_area, area)

            stack.append(i)

        return max_area