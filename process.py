import subprocess

from time import sleep

init = subprocess.Popen(
    ['dnf', 'install', 'htop-3.0.2-1.fc33.x86_64', '-y']  # f33
    # ['dnf', 'install', 'htop-2.2.0-8.fc32.x86_64', '-y'],  #f32
    # stdout=subprocess.PIPE,
    # stderr=subprocess.PIPE,
    )

init.wait()

update = subprocess.Popen([
    'dnf', 'update', 'htop'],
    stdin=subprocess.PIPE,
    # stdout=subprocess.PIPE,
    # stderr=subprocess.PIPE
)

# this is necessary to let update resolve the transaction
# before remove uninstalls the package.
sleep(2)

remove = subprocess.Popen(
    ['dnf', 'remove', 'htop', '-y'],
    # stdout=subprocess.PIPE,
    # stderr=subprocess.PIPE
)

stdout_u, stderr_u = update.communicate(input=b'y\n')

# print(stdout_u)
# print(stderr_u)
