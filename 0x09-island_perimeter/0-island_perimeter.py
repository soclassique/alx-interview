#!/usr/bin/python3
""" Function to find perimeter """


def island_perimeter(grid):
    """
    Input: List of Lists
    Returns: Perimeter of the island
    """
    count = 0
    row = len(grid)
    col = len(grid[0]) if row else 0

    for ln in range(len(grid)):
        for br in range(len(grid[ln])):

            isx = [(ln - 1, br), (ln, br - 1), (ln, br + 1), (ln + 1, br)]
            check = [1 if k[0] in range(row) and k[1] in range(col) else 0
                     for k in isx]

            if grid[ln][br]:
                count += sum([1 if not r or not grid[k[0]][k[1]] else 0
                              for r, k in zip(check, isx)])

    return (count)
