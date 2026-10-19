class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #heapify(list), 
        #heappop(heap) [popper øverste aka mindste element], 
        #heappush(list, integer)

        # Sæt listen i en maxheap, så de 2 øverste altid er i O(1) search time
        # Hvis 1. og 2. har samme vægt, er de ude og vi gentager loopet
        # Hvis den tungeste er tungere end den næsttungeste: næsttungeste er ude og tungeste har nu vægten af differencen af de to og genindsættes i heapen på dens nye plads. 
        # Fortsæt så længe stones length > 1
        # Returner vægten af den sidste hvis den eksistere, ellers 0 hvis tom liste
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            frst = heapq.heappop(stones)
            scnd = heapq.heappop(stones)
            print(frst,scnd)
            if frst == scnd:
                continue
            heapq.heappush(stones, frst-scnd)
        return 0 if not stones else -1*stones[0]