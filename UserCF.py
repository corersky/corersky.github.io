import math

def UserSimilarity(train):
	item_users = dict()
	for u,items in train.items():
		for i in items:
			if i not in item_users:
				item_users[i]=set()
			item_users[i].add(u)
	print  item_users
#{'a': set(['A', 'B']), 'c': set(['B', 'D']), 'b': set(['A', 'C']), 'e': set(['C', 'D']), 'd': set(['A', 'D'])}
	C = dict()
	N = dict()
	for i , users in item_users.items():
		for u in users:
			N.setdefault(u,0)
			N[u] += 1
			for v in users:
				if u == v:
					continue
				C.setdefault(u,{})
				C[u].setdefault(v,0)
				C[u][v] += 1
	print  C
	print  N

#{'A': {'C': 1, 'B': 1, 'D': 1}, 'C': {'A': 1, 'D': 1}, 'B': {'A': 1, 'D': 1}, 'D': {'A': 1, 'C': 1, 'B': 1}}
#{'A': 3, 'C': 2, 'B': 2, 'D': 3}
	W = dict()
	for u , related_users in C.items():
		for v , cuv in related_users.items():
			W.setdefault(u,{})
			W[u].setdefault(v,0)
			W[u][v] = cuv / math.sqrt(N[u] * N[v])
	return W


#TOP[N]
def Recommend(user,train,W,K=3):
	rank = dict()
	interacted_items = train [user]
	print interacted_items

	for v,wuv in sorted(W[user].items(),key=lambda x:x[1],reverse=True)[0:K]:
		for i in train[v]:
			if i in interacted_items:
				continue
			rank.setdefault(i,0) 
			rank[i] += wuv
	return rank

train={'A':['a','b','d'],'B':['a','c'],'C':['b','e'],'D':['c','d','e']}
F = UserSimilarity(train)
print F
#{'A': {'C': 0.4082482904638631, 'B': 0.4082482904638631, 'D': 0.3333333333333333}, 'C': {'A': 0.4082482904638631, 'D': 0.4082482904638631}, 'B': {'A': 0.4082482904638631, 'D': 0.4082482904638631}, 'D': {'A': 0.3333333333333333, 'C': 0.4082482904638631, 'B': 0.4082482904638631}}

R=Recommend('A',train,F,3)

print R

#{'c': 0.7415816237971964, 'e': 0.7415816237971964}
