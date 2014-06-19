def convert(path):
	import csv
	with open(path) as f:
		edges = [tuple(line) for line in csv.reader(f)]
	labels = node(edges)
	idxs = dict(zip(labels, range(len(labels))))
	iedges = [(idxs[e[0]], idxs[e[1]]) for e in edges]
	file = open('graph.gml', 'w')
	file.write('graph\n')
	file.write('[\n')
	for i in range(len(labels)):
		file.write('\tnode\n')
		file.write('\t[\n')
		file.write('\tid %s\n'%(i))
		file.write('\tlabel %s\n'%(str(labels[i])))
		file.write('\t]\n')
	for j in iedges:
		s = j[0]
		t = j[1]
		file.write('\tedge\n')
		file.write('\t[\n')
		file.write('\tsource %s\n'%(s))
		file.write('\ttarget %s\n'%(t))
		file.write('\t]\n')
	file.write(']\n')
	file.close
def node(edges, length = False):
	names = []
	for i in edges:
		names.append(i[0])
		names.append(i[1])
	nodes = []
	for j in names:
		flag = j in nodes
		if flag == False:
			nodes.append(j)
	new = nodes.sort()
	if length == True:
		return len(nodes)
	else:
		return nodes

