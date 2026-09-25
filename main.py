import importlib
import inspect

from rich import print

TASK_ID = 15
LEETCODE_DIR = "leetcode"

TEST_CASES = {
    15: [
        ([-1, 0, 1, 2, -1, -4],),
        ([0, 1, 1],),
        ([0, 0, 0],),
    ],
}
EXPECTED_CASES = {15: [([[-1, -1, 2], [-1, 0, 1]],), ([],), ([[0, 0, 0]],)]}


def normalize(result):
    return {tuple(sorted(t)) for t in result}


module_name = f"{LEETCODE_DIR}.{TASK_ID}"
module = importlib.import_module(module_name)

Solution = module.Solution

methods = [
    name
    for name, func in inspect.getmembers(Solution, predicate=inspect.isfunction)
    if not name.startswith("__")
]

if len(methods) != 1:
    raise RuntimeError(f"Ожидался один метод Solution, найдены: {methods}")

method_name = methods[0]
method = getattr(Solution(), method_name)


for i, args in enumerate(TEST_CASES[TASK_ID]):
    expected = EXPECTED_CASES[TASK_ID][i][0]
    result = method(*args)
    if result is None:
        print(f"{method_name}{args} -> None | False")
        continue
    is_correct = normalize(result) == normalize(expected)
    color_block = "[red]"
    if is_correct:
        color_block = "[green]"
    print(f"{method_name}{args} -> {result} | {color_block}{is_correct}")
