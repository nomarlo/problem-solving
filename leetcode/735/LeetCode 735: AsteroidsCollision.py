class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        remaining_asteroids = []
        
        for asteroid in asteroids:
            if asteroid > 0:
                remaining_asteroids.append(asteroid)
                continue            
            
            while remaining_asteroids and 0 < remaining_asteroids[-1] < abs(asteroid):
                remaining_asteroids.pop()
                
            if not remaining_asteroids or remaining_asteroids[-1] < 0:
                remaining_asteroids.append(asteroid)
                continue
            
            if remaining_asteroids[-1] == abs(asteroid):
                remaining_asteroids.pop()
                continue               
            
                
        
        return remaining_asteroids
