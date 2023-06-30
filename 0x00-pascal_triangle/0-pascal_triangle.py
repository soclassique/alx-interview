def generate_pascal_triangle(num_rows):
    triangle = []
    for i in range(num_rows):
        row = [1]  # First element of each row is always 1
        if triangle:
            prev_row = triangle[-1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)
    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(" ".join(str(num) for num in row))

# Example usage
rows = 5
pascal_triangle = generate_pascal_triangle(rows)
print_pascal_triangle(pascal_triangle)
