import sys

class CustomList(list):

    def __init__(self, custom_list: list):

        super().__init__(custom_list if custom_list else ["x"])

    def modify_line(self, line_num: int, change: str) -> list:

        if not self:
            print("The list has no line to be change. Please add one before proceeding")

            return
            
        self[line_num] = change
        
        return self
    
    def add_lines(self, number: int) -> None:

        self.extend(["x"] * number)
        return self
    
    def clear_line(self, line_num: int) -> list:
        
        if not self:
            print("The list can not be clear. Please add one before proceeding")

            return
            
        self[line_num] = "x"

        return self
    
    def clear_lines(self) -> list:

        if not self:
            print("The list can not be clear. Please add a line before proceeding")

            return
        
        self[:] = ["x"] * len(self)

        return self
    
    def remove_line(self, line_num: int) -> None:

        if not self:

            print("The list can not have a line to be remove. Please add a line before doing this")
            return
        
        self.pop(line_num)
        return self
     
    def add_mark(self, line_num: int, mark: str) -> None:

        if not self:
            print("The list can not have a line to be remove. Please add one before doing this")

            return
        
        self[line_num] = f"{self[line_num]} {mark}"
        return self
    
    def save_list(self, wanted_name: str) -> None:

        if not self:
            print("The list has no lines that can be saved. Please add a line before proceeding")
            
            return
        
        with open(wanted_name, "w") as file:

            for line in self:
                file.write(str(line) + "\n")
        
        print(f"File \"{wanted_name}\" saved successfully!")
        sys.exit()