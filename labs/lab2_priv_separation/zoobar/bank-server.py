#!/usr/bin/env python2
#
# Insert bank server code here.

#!/usr/bin/env python2
#
# Insert bank server code here.
#
import rpclib
import sys
import bank
from debug import *
import auth_client


def serialise_msg(sql_obj):
    return {c.name: getattr(sql_obj, c.name) for c in sql_obj.__mapper__.columns}

class BankRpcServer(rpclib.RpcServer):
  
    def rpc_transfer(self,sender, recipient, zoobars):
        return bank.transfer(sender, recipient, zoobars)

    def rpc_balance(self, username):
        return bank.balance(username)

    def rpc_get_log(self, username):
        res =  bank.get_log(username) # this function is crashing, with error that data is not a JSON - suspect is rpc issue
        return [serialise_msg(x) for x in res]

    def rpc_account_creation(self, username):
        return bank.account_creation(username)

(_, dummy_zookld_fd, sockpath) = sys.argv

s = BankRpcServer()
s.run_sockpath_fork(sockpath)
