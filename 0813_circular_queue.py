Q_size = 4
cQ = [0]*Q_size
front = rear = 0

rear = (rear+1)%Q_size    #enq(1)
cQ[rear] = 1

rear = (rear+1)%Q_size    #enq(2)
cQ[rear] = 2

rear = (rear+1)%Q_size    #enq(3)
cQ[rear] = 3

front = (front+1)%Q_size
print(cQ[front])

front = (front+1)%Q_size
print(cQ[front])

front = (front+1)%Q_size
print(cQ[front])

rear = (rear + 1) % Q_size  #enq(10)
cQ[rear] = 10

rear = (rear + 1) % Q_size  #enq(20)
cQ[rear] = 20