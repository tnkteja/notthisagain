a=[[1,2,3],[4,5,6],[7,8,9]]

right=lambda x,y:  (x+1,y)
down=lambda x,y:  (x,y+1)
bottomleft=lambda x,y: (x-1,y-1)
topright=lambda x,y: (x-1,y+1)

def diagonalTraverse(a,m,n):
    x,y=0,0
    count=3
    while (x,y) != (m-1,n-1) and count > 0:
        count-=1
        print y,x

        while x>0:
            x,y=topright(x,y)
            print y,x

        if y< m:
            x,y=right(x,y)
        else:
            x,y=down(x,y)

        print y,x

        while y>0:
            x,y=bottomleft(x,y)
            print y,x
        
        if x<n:
            x,y=down(x,y)
        else:
            x,y=down(x,y)
        


diagonalTraverse(a, 3, 3)