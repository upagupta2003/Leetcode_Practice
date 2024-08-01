class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top_row_bound, bottom_row_bound = 0, len(matrix)-1
        left_col_bound, right_col_bound = 0, len(matrix[0])-1
        rows, columns = len(matrix), len(matrix[0])
        res = []

        #print(f"before_loop  top_row_bound: {top_row_bound}, bottom_row_bound: {bottom_row_bound}, left_col_bound:{left_col_bound}, right_col_bound: {right_col_bound}")
        while len(res) < rows*columns:
            
            for j in range(left_col_bound,right_col_bound+1):
                res.append(matrix[top_row_bound][j])
            top_row_bound += 1
            #print(f"left2right result_arr: {res}")

            
            for i in range(top_row_bound,bottom_row_bound+1):
                res.append(matrix[i][right_col_bound])
            right_col_bound = right_col_bound - 1
            #print(f"top2bottom result_arr: {res}")

            if top_row_bound <= bottom_row_bound:
                for j in range(right_col_bound,left_col_bound-1, -1):
                    res.append(matrix[bottom_row_bound][j])
                bottom_row_bound -= 1
            #print(f"right2left result_arr: {res}")

            if left_col_bound <= right_col_bound:
                for i in range(bottom_row_bound,top_row_bound-1,-1):
                    res.append(matrix[i][left_col_bound])
                left_col_bound += 1
            # print(f"bottom2up result_arr: {res}")
            # print(f"in_the_loop  top_row_bound: {top_row_bound}, bottom_row_bound: {bottom_row_bound}, left_col_bound:{left_col_bound}, right_col_bound: {right_col_bound}")
        return res
            



            




        
        
