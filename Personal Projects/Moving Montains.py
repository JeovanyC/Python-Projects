import time


def main ():
    lines = getLines()

    for i in range(len(lines[0])):
        line = "".join(line[i] for line in lines)
        print(line)
        time.sleep(0.1)


def getMontains():
    print(
'''Hello

Want to have little heads up? Please, tell me or name.

''' )
    while True:
        name = input("> ")
        if name.isnumeric() or name == "":
            print("What?...")
        else:
            cliffs = '''
       @@      @@@@@@                                          @@@@@@    @@@@@@@@@ @@@@@@   
      @@ @@@@@@@@@@@@@@@@@                                       @@@@@@@@@@@@@@@@@@@@@@@@@  
          @@@@@@@@ @                                   /\            @@@@@@@@     @@@@      
                                                      /**\                                  
                                                     /****\                                 
                                         /\          /*** *\             And now, see!      
                                        /**\       / * ** * \                               
                                  @@    /** \     /*  *   *  \           {} moving montains!
                                  @-@  /   * \   /   *        \                             
             I'm moving          _-|_/       \  /             \                             
              Montains!         /             \/               \                            
            /                   /              /                \                           
         ()                    /             /                   \                          
        _|-                  /             /                     \                          
        /\                  /      /\     /                       \                         
                           /      / \    /                         \                        
                          /       /   \  /                           \                      
                          /      /     \/                             \                     
                         /     /       /                              \                     
________________________/_____/_______/________________________________\_____________________
'''.format(name)
    
            return cliffs
        
        continue

def getLines():
    montains = getMontains()

    numLines = montains.splitlines()
    num_Lines = max(len(numLine) for numLine in numLines)

    lines = [""] * num_Lines

    for numLine in numLines:
        for i in range(num_Lines):
            lines[i] += numLine[i] if i < len(numLine) else " "
    return lines

    
if __name__ == "__main__":
    main()