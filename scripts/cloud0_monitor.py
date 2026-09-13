import os, pyone

one = pyone.OneServer('http://%s:2633/RPC2' % os.environ['NODE2_IP'],
                      session=os.environ['ONE_AUTH'])

print('--- USERS ---')
for u in one.userpool.info().USER:
    print(u.ID, u.NAME, u.GNAME)

print('--- HOSTS ---')
for h in one.hostpool.info(-2, -1, -1).HOST:
    print(h.NAME, 'state', h.STATE)

print('--- VMs ---')
for v in one.vmpool.info(-2, -1, -1, -1).VM:
    print(v.ID, v.NAME, 'state', v.STATE, 'owner', v.UNAME)