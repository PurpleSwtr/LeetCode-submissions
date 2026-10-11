class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i, matr in enumerate(image):
            image[i] = [num ^ 1 for num in matr[::-1]]
        return image
