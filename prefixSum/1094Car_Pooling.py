class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda row:row[1])
        pas=0
        end=trips[0][2]
        pq=[]
        key_to_value=defaultdict(int)

        for  x in trips:
            if pq!=[]:
                top=pq[0]
            else:
                top=99999
            key_to_value[x[2]]+=x[0]
            heapq.heappush(pq,x[2])
            while x[1]>=top:
                pas-=key_to_value[top]
                key_to_value[pq[0]]=0
                heapq.heappop(pq)
                top=pq[0]
            pas+=x[0]
            if(pas>capacity):
                return False

        return True
