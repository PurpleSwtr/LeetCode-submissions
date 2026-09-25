import random


class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        return True if len(set(nums)) == len(nums) else False


s = Solution()
nums = [1, 2, 3, 3]
print(s.hasDuplicate(nums))


items = ["💎", "⚔️", "🏹"]

random.choice()

biomes = [
    "🌲 Тайга",
    "🏜️ Пустыня",
    "❄️ Ледяная равнина",
    "🌿 Джунгли",
    "🍄 Грибные поля",
]


import random

offers = [
    " 💎 1 алмаз ",
    "🥕 20 морковок",
    "📚 Зачарованная книга",
    "⛏️ Алмазная кирка",
]

random.shuffle(items)

print(items)
