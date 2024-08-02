class Solution:

    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        def invert_image(image: list[list]):
            for i in range(len(image)):
                for j in range(len(image)):
                    if image[i][j] == 1:
                        image[i][j] = 0
                    else:
                        image[i][j] = 1
            return image
        
        if n <= 1:
            image = invert_image(image)
            return image

        image = invert_image(image)
        left_bound = 0
        right_bound = len(image[0])-1

        while left_bound < right_bound:
            for i in range(len(image)):
                image[i][left_bound], image[i][right_bound] = (
                    image[i][right_bound],
                    image[i][left_bound],
                )
            left_bound += 1
            right_bound -= 1
        return image

