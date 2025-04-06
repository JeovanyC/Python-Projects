import tabulate as tl

available_fonts = [
    "plain", "simple", "github", "grid", "simple_grid", 
    "rounded_grid", "heavy_grid", "mixed_grid", "double_grid", 
    "fancy_grid", "outline", "simple_outline", "rounded_outline", 
    "heavy_outline", "mixed_outline", "double_outline", "fancy_outline", 
    "pipe", "orgtbl", "asciidoc", "jira", "presto", "pretty", 
    "psql", "rst", "mediawiki", "moinmoin", "youtrack", 
    "html", "unsafehtml", "latex", "latex_raw", "latex_booktabs", 
    "latex_longtable", "textile", "tsv"
]

def valid_fonts() -> str:

    print('''
Can you tell us what font do you want to use?
          
(F to show fonts)''')

    while True:

        font = input("> ").strip().lower()

        if font == "f":

            print()

            print_list(available_fonts, "simple_grid")

            print()

            continue

        if not font:
            return "plain"

        if not font in available_fonts:
            
            print("That is not one of our available fonts. Please, try again")
            continue

        return font
    
def print_list(any_list: list, font: str) -> None:

    any_list = [[idx, item] for idx, item in enumerate(any_list, start=1)]

    print(tl.tabulate(any_list, tablefmt=font))

def print_table(any_table: list, font: str) -> None:

    header_index = [" "] + [str(i + 1) for i in range(len(any_table[0]))]

    indexed_table = [header_index] + [[str(i +1)] + row for i, row in enumerate(any_table)]
                             
    print(tl.tabulate(indexed_table, tablefmt=font))