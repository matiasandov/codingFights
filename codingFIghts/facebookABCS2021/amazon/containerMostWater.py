class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        
        #buscar desde los lados
        l = 0
        r = len(height)-1
        #ir avanzando hacia los mas grandes hasta que se intersecten
        while l<r:
            cur = (r-l) * min(height[l], height[r])
            area = max(cur, area)

            #el mas grande se queda fijo y el mas chico se salta izq o der
            if height[r] > height[l]:
                l+=1
            else:
                r-=1
        return area