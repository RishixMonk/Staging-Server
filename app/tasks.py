from celery import shared_task
from .getport import find_free_port
from subprocess import PIPE, run

# def test_func(self):
#     for i in range(10):
#         print(i)
#     return "Done"


@shared_task(bind=True)
def deployFromImage(self,dockerImage,internalPort, externalPort):
    # dockerImage = "tutum/hello-world:latest"
    # internal_port = "3000"
    # externalport = find_free_port(),
    # check if container is already running
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