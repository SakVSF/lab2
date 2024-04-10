from debug import *
from zoodb import *
import rpclib




def transfer(sender, recipient, zoobars):
    ## Fill in code here.
    with rpclib.client_connect('/banksvc/sock') as c:
        return c.call('transfer', sender=sender, recipient=recipient, zoobars=zoobars)

def balance(username):
    ## Fill in code here.
    with rpclib.client_connect('/banksvc/sock') as c:
        return c.call('balance', username=username)

def get_log(username):
    ## Fill in code here.
    with rpclib.client_connect('/banksvc/sock') as c:
        return c.call('get_log', username=username)

def account_creation(username):
    ## Fill in code here.
    with rpclib.client_connect('/banksvc/sock') as c:
        return c.call('account_creation', username=username)
