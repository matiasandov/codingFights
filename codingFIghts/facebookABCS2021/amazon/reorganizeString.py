class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        1. dicc frecc y crear un stack y agregar
        2. sort by freq

        3. crear nueva string mientras dando ciclos en el dicc y mientras su freq sea mayor a cero append a nueva string
        
        """

        dicc = {}
        
        for i in s:
            if i in dicc:
                dicc[i] += 1
            else:
                dicc[i] = 1
        
        #no necesito ordenar porque minHeap los ordena 
        minHeap = []
        for k, v in dicc.items():
            minHeap.append([-v, k])
        
        heapq.heapify(minHeap)
        print(minHeap)
        prev = None
        new = ""
        
        while minHeap or prev:
            #si sobro un par por comparar pero ya no hay nada en el minheap quiere decir que ya no queda nada por intercambiar
            if prev and not minHeap:
                return ""
            
            cnt, val = heapq.heappop(minHeap)
            new += val
            cnt +=1

            #antes de crear otro prev debo checar si ya existe uno para agregarlo
            if prev:
                heapq.heappush(minHeap, prev)
                prev = None
            
            #si aun es usable
            if cnt < 0:
                prev = [cnt, val]
        
       
        return new
