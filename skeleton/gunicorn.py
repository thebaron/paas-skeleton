import os
import os.path

PROJECT_HOME_DIR = os.environ.get('PROJECT_HOME_DIR', '..')
PROJECT_NAME = os.environ.get('PROJECT_NAME', 'skeleton')
VE_ROOT = os.environ.get('VE_ROOT')
PROJECT_RUN_DIR = os.environ.get('OPENSHIFT_PATTON_RUN_DIR', VE_ROOT + '/var/run')

OPENSHIFT_PATTON_IP = os.environ.get('OPENSHIFT_PATTON_IP', '127.0.0.1')
OPENSHIFT_PATTON_PORT = os.environ.get('OPENSHIFT_PATTON_PORT', '')

# make directory if needed
if not os.path.exists(PROJECT_RUN_DIR):
    os.makedirs(PROJECT_RUN_DIR)

# 
# if you want to bind to unix domain socket for nginx
# bind = 'unix:%s/%s.sock' % (PROJECT_RUN_DIR, PROJECT_NAME)
#
bind = '%s:%s' % (OPENSHIFT_PATTON_IP, OPENSHIFT_PATTON_PORT)

daemon = False
max_requests = 1000
timeout = 600
pidfile = '%s/%s.pid' % (PROJECT_RUN_DIR, PROJECT_NAME)
preload = True
secure_scheme_headers = {'X-FORWARDED-PROTO': 'https'}
worker_class = 'sync'
# worker_connections = 250
workers = 5
