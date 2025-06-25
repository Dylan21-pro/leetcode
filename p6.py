class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: when zigzag isn't needed
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of strings for each row
        rows = ['' for _ in range(numRows)]
        current_row = 0
        direction = 1  # 1 for down, -1 for up

        for char in s:
            rows[current_row] += char

            # Change direction at the top or bottom
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        # Join all rows into a single string
        return ''.join(rows)
