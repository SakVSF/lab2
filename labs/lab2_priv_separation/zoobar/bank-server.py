#!/usr/bin/env python2
#
# Insert bank server code here.

#

import rpclib 
import sys
import bank
from debug import *
from sqlalchemy.orm import class_mapper

def serialise(model):
    cols = [i.key for i in class_mapper(model.__class__).columns]
    return dict((i, getattr(model, i)) for i in cols)

class BankRpcServer(rpclib.RpcServer):
    def rpc_transfer(self, sender, recipient, zoobars):
        return bank.transfer(sender, recipient, zoobars)

    def rp_balance(self, username):
        return bank.balance(username)

    def rpc_get_log(self, username):
        return [serialise(log) for log in bank.get_log(username)]

    def rpc_account_creation(self, username):
        return bank.account_creation(username)


(_, dummy_zookld_fd, sockpath) = sys.argv

s=BankRpcServer()
s.run_sockpath_fork(sockpath)


