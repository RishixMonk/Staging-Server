# from rq import Queue
# from redis import Redis 
from .getport import find_free_port
from .tasks import deployFromImage
# # Tell RQ what Redis connection to use
# redis_conn = Redis()
# q = Queue(connection=redis_conn)  # no args implies the default queue

def f1():
    # while True:
        dockerimage = input("\nEnter docker image name : ")
        # externalport = input("\nEnter external port : ")
        internalport = input("\nEnter internal port : ")
        externalport = find_free_port()
        print(f"\nExternal port is {externalport}")
        return dockerimage,internalport
        # try:
        #     job = q.enqueue(
        #         deployFromImage, 
        #             dockerimage,
        #             externalport,
        #             internalport,
        #         job_timeout=600  # 10 minutes
        #         )
        #     print(f"\njob {job.get_id()} -> {dockerimage} is queued\n")
        # except:
        #     print("Error in deployment\n\n")
        
