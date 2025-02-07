class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        prefix=[[0]*n for i in range(n)]
        for x in queries:
            r1=x[0]
            c1=x[1]
            r2=x[2]
            c2=x[3]
            while(r1<=r2):
                prefix[r1][c1]+=1
                if c2+1<n:
                    prefix[r1][c2+1]-=1
                r1+=1
        # print(prefix)
        for i in range(n):
            p=0
            for j in range(n):
                p+=prefix[i][j]
                prefix[i][j]=p
        return prefix