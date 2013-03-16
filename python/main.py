# -*- coding:utf8 -*-
import math
class Item:
    def __init__(self, iid):
        # item id
        self.iid = iid 
        # store user->ratting
        self.user = {}
        self.sum = 0.0

class Message:
    def __init__(self, user, iid, ratting):
        self.user = user
        self.iid = iid
        self.ratting = ratting


class Algorithm:
    '''
        An CF Algorithm Implement
    '''
    def __init__(self):
        # items:{iid:Item}
        self.items = {}
        self.users = {}

    def caculate_result(self):
        for iid in self.items.keys():
            # caculate result item: iid
            print 'iid:%s\tresult:' % iid
            result_dict = {}
            for iid2 in self.items.keys():
                if iid != iid2:
                    doc_sum = 0.0
                    user1 = self.items[iid].user
                    user2 = self.items[iid2].user
                    for gid in user1:
                        if gid in user1.keys():
                            doc_sum = user1[gid] * user2[gid]
                    result = doc_sum / math.sqrt(self.items[iid].sum)
                    result_dict.update({iid2:result})
            print result_dict

    def read_message(self, message):
        user = message.user
        iid = message.iid
        ratting = message.ratting
        # update iid info
        if self.items.has_key(iid):
            if self.items[iid].user.has_key(user):
                if self.items[iid].user[user] < ratting:
                    # update sum
                    self.items[iid].sum = self.items[iid].sum - \
                        self.items[iid].user[user] ** 2 + ratting ** 2
                    self.items[iid].user[user] = ratting
            else:
                self.items[iid].sum = ratting ** 2
                self.items[iid].user.update({user:ratting})
        else:
            item = Item(iid)
            item.sum = ratting ** 2
            item.user.update({user:ratting})
            self.items.update({iid:item})

    def output(self):
        for iid in self.items.keys():
           print 'iid: %s' % iid
           for gid in self.items[iid].user:
                print '\tuser: %s, ratting: %s' % (gid, self.items[iid].user[gid])

if __name__ == '__main__':
    alg = Algorithm()
    m1 = Message(2, 1, 1)
    m2 = Message(1, 2, 1)
    m3 = Message(2, 2, 1)
    m4 = Message(1, 1, 1)
    alg.read_message(m1)
    alg.read_message(m2)
    alg.read_message(m3)
    alg.read_message(m4)
    alg.caculate_result()
    #alg.output() 
