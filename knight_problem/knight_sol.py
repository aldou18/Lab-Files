def knight_probability(size, moves, r_start, c_start):
    directions = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    from functools import lru_cache
    
    @lru_cache(None)
    def dp(m, r, c):
        if r < 0 or r >= size or c < 0 or c >= size:
            return 0
        if m == 0:
            return 1
        
        prob = 0
        for dr, dc in directions:
            prob += dp(m - 1, r + dr, c + dc) / 8.0
        return prob

    return dp(moves, r_start, c_start)


# Example:
print(knight_probability(3, 2, 0, 0))  # Expected: 0.0625