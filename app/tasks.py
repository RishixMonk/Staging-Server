from celery import shared_task
from .getport import find_free_port
from subprocess import PIPE, run

# def test_func(self):
#     for i in range(10):
#         print(i)
#     return "Done"


@shared_task(bind=True)
def deployFromImage(self,dockerImage,externalPort=find_free_port(),internalPort="3000"):
    # dockerImage = "tutum/hello-world:latest"
    # internal_port = "3000"
    # externalport = find_free_port(),
    # check if container is already running
    res = run(
        ['docker', 'ps', '-a', '--format', '{{.Names}}'],
        stdout=PIPE,
        stderr=PIPE,
    )
    if dockerImage in res.stdout.decode('utf-8'):
        print(f"Container {dockerImage} already exists")
        opt = input("Do you want to redeploy? (y/n)")
        if opt == 'y' or opt == 'Y':
            # stop the container
            res = run(
                ['docker', 'stop', dockerImage],
                stdout=PIPE,
                stderr=PIPE,
            )
            # remove the container
            res = run(
                ['docker', 'rm', dockerImage],
                stdout=PIPE,
                stderr=PIPE,
            )
        else:
            print("Exiting")
            return "Container already exists"

    print(f"Deploying {dockerImage} on port {externalPort}:{internalPort}")
    res = run(
        ['docker', 'run','-d', '-p', f'{externalPort}:{internalPort}', dockerImage],
        stdout=PIPE,
        stderr=PIPE,
    ) 
    print(res.stderr.decode('utf-8'))
    print(res.stdout.decode('utf-8'))
    return

# def getLogs(dockerImage):
#     res = run(
#         ['docker', 'logs', f'{dockerImage}container'],
#         stdout=PIPE,
#         stderr=PIPE,
#     )
#     return res.stdout.decode('utf-8')