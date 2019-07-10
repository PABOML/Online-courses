# python3
import random
class JobQueue:
    def read_data(self):
        self.num_workers, self.m = map(int, input().split())
        #print(m)
        self.jobs = list(map(int, input().split()))
        assert self.m == len(self.jobs)
        
        #.... Stress test....
    def StressTest(self):    
        self.num_workers, self.m = random.randint(1,100000), random.randint(1,100000)
        self.jobs = [random.randint(0,1000000000) for i in range(self.m)]
            
        #....................
        
    def write_response(self):
        #if self.assigned_workers == self.assigned_workers_n and self.start_times == self.start_times_n:
        #    print('Correct')
        for i in range(len(self.assigned_workers)):
          print(self.assigned_workers[i], self.start_times[i])
        
    def write_response_naive(self):
        for i in range(self.m):
          print('n',self.assigned_workers_n[i], self.start_times_n[i])
        

#.........SiftDown code from previous assignment, adapted.................
    def SiftDown(self):
        self.maxIndex = self.i
        l = 2*self.i + 1 # left Child
        r = 2*self.i + 2 # right Child
        
        if (l <= (len(self.min_heap)-1) and self.min_heap[l][1] < self.min_heap[self.maxIndex][1]) or (l <= (len(self.min_heap)-1) and self.min_heap[l][1] == self.min_heap[self.maxIndex][1] and self.min_heap[l][0] < self.min_heap[self.maxIndex][0]) :
            self.maxIndex = l
            
        if (r <= (len(self.min_heap)-1) and self.min_heap[r][1] < self.min_heap[self.maxIndex][1]) or (r <= (len(self.min_heap)-1) and self.min_heap[r][1] == self.min_heap[self.maxIndex][1] and self.min_heap[r][0] < self.min_heap[self.maxIndex][0]) :
            self.maxIndex = r
            
        if self.i != self.maxIndex:
            self.min_heap[self.i], self.min_heap[self.maxIndex] = self.min_heap[self.maxIndex], self.min_heap[self.i]
            self.i = self.maxIndex
            self.SiftDown()    
#..........................................................................
    def SiftUp(self):
        
        while ( self.i > 0 and self.min_heap[ (self.i - 1) // 2 ][1] > self.min_heap[self.i][1] ) or (self.i > 0 and self.min_heap[ (self.i - 1) // 2 ][1] == self.min_heap[self.i][1] and self.min_heap[ (self.i - 1) // 2 ][0] > self.min_heap[self.i][0]):
            self.min_heap[ (self.i - 1) // 2 ], self.min_heap[self.i] = self.min_heap[self.i], self.min_heap[ (self.i - 1) // 2 ]
            self.i = (self.i - 1 // 2)
    
    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
    #........................Pauls code.........................
        self.assigned_workers = []
        self.start_times = []
        if self.num_workers >= self.m:
            for self.i in range(0, self.num_workers) :
                self.assigned_workers.append(self.i)
            self.start_times = [0] * len(self.jobs)
        else:    
            # Build the initial heap:
            self.min_heap=[]
            for self.i in range(0, min(self.num_workers,self.m) ):
                self.min_heap.append((self.i, 0))  
        
            # Iterate through the job list
            while self.jobs:
                job = 0
                current_job = self.min_heap.pop(0)
                
                while job == 0 and self.jobs: # if job has length 0, assign it right away
                    job = self.jobs.pop(0) 
                    self.assigned_workers.append(current_job[0])
                    self.start_times.append(current_job[1])
            
                self.min_heap.insert( 0, (current_job[0], current_job[1] + job) )
                #self.min_heap.append( (current_job[0], current_job[1] + job) )
                #After each new insert of root, call SiftDown to sort heap
                #self.i  = len(self.min_heap) - 1
                self.i = 0
                self.SiftDown()
                #print(self.min_heap)
                                         
    
    
    #...........................................................
    def assign_jobs_naive(self):   
        
        self.assigned_workers_n = [None] * len(self.jobs)
        self.start_times_n = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers_n[i] = next_worker
          self.start_times_n[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]
        
    def solve(self):
        self.read_data()
        #self.StressTest()
        #self.assign_jobs_naive()
        self.assign_jobs()
        self.write_response()
        #self.write_response_naive()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

