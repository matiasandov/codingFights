"""
1. ordenar las 3 listas por username, timestamp 
2. crear un dicc de listas donde sera muy sencillo agregar cosas
3. agregar a cada usuario las listas ordenadas

contar freq
crear dicc de freq
para cada usuario acceder a su lista
con su lista crear todas las posibles combinaciones con itertools.combinations(sites, 3)
4. si combinacion en dicc sumar y sino agregar
5. encontrar la combinacion con freq max y si ya existe algo del mismo tamano compara lexicamente y reemplazas

"""

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:


        threeLists = sorted(zip(username,timestamp, website))
        graph = defaultdict(list)
        #los 3 iteradores son necesarios para recorrer zip
        for user,t, site in threeLists:
            graph[user].append(site)

        freq = {}

        for u, sites in graph.items():
            #tiene que ser una lista 
            combos = set(itertools.combinations(sites,3))
            print(combos)
            for seq in combos:
                if seq in freq:
                    freq[seq] += 1
                else:
                    freq[seq] = 1
        
        res = None
        maxFreq = 0

        for seq, f in freq.items():
            if f > maxFreq:
                maxFreq = f
                res = seq
            elif f == maxFreq and seq < res:
                res = seq
        return res