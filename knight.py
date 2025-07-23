def knight_probability(size, moves, r_start, c_start):
    #first check --> what are the squares around me
    # second check --> all the moves possible (including the invisible) --> coordinates including negative ones
    # third check --> which coordinates are both positive --> that square is available
    # add the positve ones and then divide it by 8

    """
    All possible moves on the board:
    UPPER LEFT
    Move1: 2 left 1 up
    Move2: 2 up 1 left

    UPPER RIGHT
    Move3: 2 right 1 up
    Move4: 2 up 1 right

    LOWER LEFT
    Move5: 2 left 1 down
    Move6: 2 down 1 left

    LOWER RIGHT
    Move7: 2 right 1 down
    Move8: 2 down 1 right

    """

    #setting up the grid
    grid = [[0 for i in range(size)] for i in range(size)]
    grid[r_start][c_start] = 'X'
    for row in range(len(grid)-1,-1,-1):
        print(grid[row])

    total_potential_moves = moves * 8
    total_moves_available = []
    
    def is_valid_move(coord):
        for i in coord:
            if i < 0 or i > size-1:
                return False
            else:
                pass
            
        return True


    def checkmoves(r,c, moves):
        if moves == 0:
            return
        
        sections = {"upperleft":[[r-1,c-2],[r-2,c-1]],
                    "upperright": [[r-1,c+2],[r-2,c+1]],
                    "lowerleft": [[r+1,c-2],[r+2,c-1]],
                    "lowerright": [[r+1,c+2],[r+2,c+1]]
                    }
    
        global moves_available
        moves_available = 8
        for section in sections.values():
            for i in range(len(section)):
                

                # I think you have to recurse in here
                new_r = section[i][0] 
                new_c = section[i][1] 
                
                if moves > 1:
                    checkmoves(new_r,new_c, moves-1)
                    
                

                print(section[i])
                print(is_valid_move(section[i]))
                if is_valid_move(section[i]) == False:
                    moves_available -= 1
                else:
                    pass

        
        total_moves_available.append(moves_available)
        return moves_available           
                
                


    checkmoves(r_start,c_start,moves)
    
    print(total_moves_available)
    probability = float(sum(total_moves_available)/total_potential_moves)

    return probability     

print(knight_probability(3,2,0,0))
