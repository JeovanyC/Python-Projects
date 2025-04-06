import sys

class CustomTable(list):

    def __init__(self, custom_table: list):

        super().__init__(custom_table if custom_table else ["x"])

    def modify_cell(self, column_num: int, row_num: int, change: str) -> list:
                
        if not self:
            print("The table has no cell to be changed. Please add a row or column before proceeding")

            return
        
        self[row_num][column_num] = change
        return self
    
    def add_column(self, number: int) -> None:

        self[:] = [row + ["x"] * number for row in self]
        return self
    
    def add_row(self, number: int) -> None:

        self += [["x"] * len(self[0])] * number  
        return self
    
    def clear_cell(self, column_num: int, row_num: int) -> list:

        if not self:
            print("The table has no cell to be clear. Please add a row or column before proceeding")

            return

        self[row_num][column_num] = "x"
        return self
    
    def clear_cells(self) -> list:
        if not self:
            print("The table has no cells to be clear. Please add a row or column before proceeding")

            return
        
        self[:] = [["x"] * len(self[0]) for _ in range(len(self))]
        return self
    
    def remove_column(self, column_num: int) -> list:
            
        if not self:
            print("The table has no column to be remove. Please add a column before proceeding")
            
            return
        
        self[:] = [[value for i, value in enumerate(row) if i != column_num] for row in self]
        return self

    def remove_row(self, row_num: int) -> list:

        if not self:
            print("The table has no row to be remove. Please add a row before proceeding")

            return
        
        self.pop(row_num)
        return self

    def save_table(self, wanted_name: str, separator: str = ", ") -> None:
        
        if not self:
            print("The table has no cells to be saved. Please add a row or column before proceeding")

            return
        
        with open(wanted_name, "w") as file:
            for line in self:

                file.write(separator.join(map(str, line)) + "\n")
        
        print(f"File \"{wanted_name}\" saved successfully!")
        sys.exit()