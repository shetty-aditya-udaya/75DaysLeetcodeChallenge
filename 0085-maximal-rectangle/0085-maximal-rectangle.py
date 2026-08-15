class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:

            # Build histogram heights
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Largest Rectangle in Histogram
            stack = []

            for i in range(cols + 1):
                curr = heights[i] if i < cols else 0

                while stack and heights[stack[-1]] > curr:
                    h = heights[stack.pop()]

                    if stack:
                        width = i - stack[-1] - 1
                    else:
                        width = i

                    max_area = max(max_area, h * width)

                stack.append(i)

        return max_area
        