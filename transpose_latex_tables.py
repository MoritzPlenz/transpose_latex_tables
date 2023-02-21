from typing import List

# put your latex table here
LATEX_TABLE = \
r"""
A1 & A2 & A3 \\
B1 & B2 & B3 \\
C1 & C2 & C3 \\
D1 & D2 & D3 \\
"""

def get_table(table:str) -> List[List[str]]:
    lines = table.strip().split(r"\\")
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line]
    lines = [line.split("&") for line in lines]
    lines = [[cell.strip() for cell in line] for line in lines]

    max_num_cols = max(len(line) for line in lines)
    lines = [line + [""] * (max_num_cols - len(line)) for line in lines]

    return lines

def transpose_table(table:List[List[str]]) -> List[List[str]]:
    num_og_cols = max(len(line) for line in table)
    new_table = [[line[i] for line in table] for i in range(num_og_cols)]
    return new_table

def print_table(table:List[List[str]]) -> None:
    for row in table:
        print(r'%s' % " & ".join(row) + r" \\")

def main(latex_table:str=LATEX_TABLE):
    og_table = get_table(latex_table)
    new_table = transpose_table(og_table)
    
    print("Original table:")
    print_table(og_table)
    print()
    print("Transposed table:")
    print_table(new_table)

if __name__ == "__main__":
    main()
