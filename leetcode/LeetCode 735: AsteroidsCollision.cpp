class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> remainingAsteroids;
        
        for(auto asteroid : asteroids){
            if(asteroid > 0){
                remainingAsteroids.push(asteroid);
                continue;
            }
            
            while(!remainingAsteroids.empty() && remainingAsteroids.top() > 0 && remainingAsteroids.top() < abs(asteroid) ){
                remainingAsteroids.pop();                
            }
            
            if (remainingAsteroids.empty() || remainingAsteroids.top() < 0 ){
                remainingAsteroids.push(asteroid);
                continue;
            }
            
            if ( remainingAsteroids.top() == abs(asteroid) ){
                remainingAsteroids.pop();
                continue;
            }
            
            
        }
        
        
        vector<int> asteroidsResult;
        while(!remainingAsteroids.empty()){
            asteroidsResult.push_back(remainingAsteroids.top());
            remainingAsteroids.pop();
        }
        
        reverse(asteroidsResult.begin(), asteroidsResult.end());
        
        return asteroidsResult;
    }
};
