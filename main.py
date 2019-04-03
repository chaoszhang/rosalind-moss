# coding: utf-8

import sys
import re
import os
import glob
from config import *
from scraper import RosalindExporter
from sets import Set

oo = 999999
INDEL = 3
GAP = 15

def export_code(url, assignment_number):
	re = RosalindExporter(url, rosalind_username, rosalind_password)
	re.set_urls_for_assignment_n(assignment_number)
	re.get_code_from_submission_urls()
	return re.codelist()

def notebook2python(txt):
	if len(txt) > 50000:
		txt = "\n".join([x for x in re.split(r'[\n\r\f\v]', txt) if x != '' and len(x) <= 300])
	if len(txt) > 50000:
		return txt
	if '"cells":' in txt:
		try:
			with open('temp.ipynb', 'w+') as to_write:
				to_write.write(txt)
			os.system('jupyter nbconvert --to script temp.ipynb')
			for file in glob.glob("temp.*"):
				if not file.endswith(".ipynb"):
					txt = open(file, 'r').read()
					#print >> sys.stderr, txt
					os.system('rm temp.*')
					return txt
			os.system('rm temp.*')
			return txt
		except:
			return txt
	return txt

def code_to_symbols(txt):
	lines = [x for x in re.split(r'[\n\r\f\v]', txt) if x != '' and len(x) <= 300]
	symbols = []
	for i in xrange(len(lines)):
		arr = [x for x in re.split(r'(\W)', lines[i]) if x != ' ' and x != '\t' and x != '']
		if len(arr) > 30:
			continue
		t = [x for x in re.split(r'[\w\s]', lines[i])]
		symbols += t
	return "".join(symbols)

def text_alignscore(a, b):
	n = len(a)
	m = len(b)
	f = []
	g = []
	for i in range(n + 1):
		f.append([])
		g.append([])
		for j in range(m + 1):
			f[i].append(0)
			g[i].append(0)
	for i in range(1, n + 1):
		for j in range(1, m + 1):
			if a[i - 1] == b[j - 1]:
				c = 1
			else:
				c = -2
			f[i][j] = max(max(f[i - 1][j - 1], g[i - 1][j - 1]) + c, max(f[i - 1][j], g[i - 1][j], f[i][j - 1], g[i][j - 1]) - INDEL)
			g[i][j] = max(g[i - 1][j], g[i][j - 1], f[i][j] - GAP)
	return g[n][m]

def code_to_concept(txt):
	lines = [x for x in re.split(r'[\n\r\f\v]', txt) if x != '' and len(x) <= 300]
	concepts = []
	lastseen = {}
	cnt = 0
	for i in xrange(len(lines)):
		arr = [x for x in re.split(r'(\W)', lines[i]) if x != ' ' and x != '\t' and x != '']
		if len(arr) > 30:
			continue
		for s in arr:
			if len(s) > 20:
				s = s[:20]
			cnt += 1
			if s in lastseen:
				shift = cnt - lastseen[s]
			else:
				shift = -1
			lastseen[s] = cnt
			concepts.append((hash(s), shift, i))
	return (concepts, lines)
	
def alignscore(a, b):
	n = len(a)
	m = len(b)
	f = []
	g = []
	for i in range(n + 1):
		f.append([])
		g.append([])
		for j in range(m + 1):
			f[i].append(0)
			g[i].append(0)
	for i in range(1, n + 1):
		for j in range(1, m + 1):
			ta = a[i - 1]
			tb = b[j - 1]
			if ta[0] == tb[0] or (ta[1] == tb[1] and ta[1] != -1):
				c = 1
			elif abs(ta[1] - tb[1]) <= 2 and ta[1] != -1 and tb[1] != -1:
				c = 0
			elif i != 1 and j != 1 and ta[1] - a[i - 2][1] == tb[1] - b[j - 2][1] and ta[1] != -1 and tb[1] != -1 and a[i - 2][1] != -1 and b[j - 2][1] != -1:
				c = 0
			else:
				c = -2
			f[i][j] = max(max(f[i - 1][j - 1], g[i - 1][j - 1]) + c, max(f[i - 1][j], f[i][j - 1]) - INDEL)
			g[i][j] = max(g[i - 1][j], g[i][j - 1], f[i][j] - GAP)
	return g[n][m]

def align(a, b, txta, txtb):
	n = len(a)
	m = len(b)
	f = []
	g = []
	for i in range(n + 1):
		f.append([])
		g.append([])
		for j in range(m + 1):
			f[i].append((-oo, -1, -1))
			g[i].append((0, -1, -1))
	for i in range(1, n + 1):
		for j in range(1, m + 1):
			ta = a[i - 1]
			tb = b[j - 1]
			if ta[0] == tb[0] or (ta[1] == tb[1] and ta[1] != -1):
				c = 1
			elif abs(ta[1] - tb[1]) <= 2 and ta[1] != -1 and tb[1] != -1:
				c = 0
			elif i != 1 and j != 1 and ta[1] - a[i - 2][1] == tb[1] - b[j - 2][1] and ta[1] != -1 and tb[1] != -1 and a[i - 2][1] != -1 and b[j - 2][1] != -1:
				c = 0
			else:
				c = -2
			if f[i][j][0] < f[i - 1][j - 1][0] + c:
				f[i][j] = (f[i - 1][j - 1][0] + c, f[i - 1][j - 1][1], f[i - 1][j - 1][2])
			if f[i][j][0] < f[i - 1][j][0] - INDEL:
				f[i][j] = (f[i - 1][j][0] - INDEL, f[i - 1][j][1], f[i - 1][j][2])
			if f[i][j][0] < f[i][j - 1][0] - INDEL:
				f[i][j] = (f[i][j - 1][0] - INDEL, f[i][j - 1][1], f[i][j - 1][2])
			if f[i][j][0] < g[i - 1][j - 1][0] + c:
				f[i][j] = (g[i - 1][j - 1][0] + c, i - 1, j - 1)
			if g[i][j][0] < g[i - 1][j][0]:
				g[i][j] = (g[i - 1][j][0], g[i - 1][j][1], g[i - 1][j][2])
			if g[i][j][0] < g[i][j - 1][0]:
				g[i][j] = (g[i][j - 1][0], g[i][j - 1][1], g[i][j - 1][2])
			if g[i][j][0] < f[i][j][0] - GAP:
				g[i][j] = (f[i][j][0] - GAP, i, j)
	
	gi = n
	gj = m
	arr = []
	while g[gi][gj][1] != -1:
		fi = g[gi][gj][1]
		fj = g[gi][gj][2]
		arr.append((f[fi][fj][1], fi, f[fi][fj][2], fj))
		gi = f[fi][fj][1]
		gj = f[fi][fj][2]
	arr = arr[::-1]
	for e in arr:
		print ">>>>>>>>>>"
		for i in range(a[e[0]][2], a[e[1] - 1][2] + 1):
			print txta[i]
		print "<<<<<<<<<<"
		for i in range(b[e[2]][2], b[e[3] - 1][2] + 1):
			print txtb[i]
		print ""
	
def main():
	url1 = 'http://rosalind.info/classes/576/students/'
	url2 = 'http://rosalind.info/classes/577/students/'
	start = 70
	end = 78
	assignment_number = range(start - 1, end)

	names = {}
	namepairs = {}
	for an in assignment_number:
		cnt = 0
		print "Q" + str(an + 1)
		print >> sys.stderr, "Q" + str(an + 1)
		submissions = export_code(url1, an) + export_code(url2, an)
		print >> sys.stderr, "Fetching Done!"
		hw = []
		for t in submissions:
			t = (t[0], t[1].encode(encoding='ascii',errors='ignore'))
			t = (t[0], notebook2python(t[1]))
			e = code_to_concept(t[1])
			if len(t[1]) > 30000 and len(e[0]) > 5000:
				print "--zc--abnormal size " + str(len(t[1])) + " for " + t[0]
				print t[1]
				t = (t[0], "")
				e = ([], [])
			elif len(t[1]) > 0 and len(t[1]) < 100:
				print "--zc--abnormal size " + str(len(t[1])) + " for " + t[0]
				print t[1]
			elif len(t[1]) >= 100:
				cnt += 1
			hw.append((e[0], e[1], t[0], t[1], code_to_symbols(t[1])))
		print >> sys.stderr, "Starting alignment round 1!"
		prescore = []
		for i in xrange(len(hw)):
			prescore.append([])
			for j in xrange(len(hw)):
				prescore[i].append((-1, 0))
		for i in xrange(len(hw)):
			for j in xrange(i):
				v = text_alignscore(hw[i][4], hw[j][4])
				prescore[i][j] = (v, j)
				prescore[j][i] = (v, i)
				
		print >> sys.stderr, "Starting alignment round 2!"
		smax = [(-1, 0, 0)] * len(hw)
		pairs = []
		for i in xrange(len(hw)):
			for e in sorted(prescore[i], reverse=True)[:5]:
				j = e[1]
				pairs.append((min(i, j), max(i, j)))
		pairs = list(Set(pairs))
		for e in pairs:
				i = e[0]
				j = e[1]
				v = alignscore(hw[i][0], hw[j][0])
				if v > smax[i][0]:
					smax[i] = (v, min(i, j), max(i, j))
				if v > smax[j][0]:
					smax[j] = (v, min(i, j), max(i, j))
		smax = list(Set(smax))
		smax.sort(reverse=True)
		try:
			print "--zc-- number of valid submissions: " + str(cnt) + ", 80% score: " + str(smax[int(cnt * 0.2)][0]) + ", median score: " + str(smax[int(cnt * 0.5)][0])
		except:
			print "--zc-- number of valid submissions: " + str(cnt)
		namemap = {}
		for i in range(5):
			name1 = min(hw[smax[i][2]][2], hw[smax[i][1]][2])
			name2 = max(hw[smax[i][2]][2], hw[smax[i][1]][2])
			print "--zc--PAIR " + str(i + 1) + ": " + name1 + " and " + name2 + " with score " + str(smax[i][0])
			align(hw[smax[i][2]][0], hw[smax[i][1]][0], hw[smax[i][2]][1], hw[smax[i][1]][1])
			print ">>>" + hw[smax[i][2]][2]
			print hw[smax[i][2]][3]
			print "<<<" + hw[smax[i][1]][2]
			print hw[smax[i][1]][3]
			if name1 not in namemap:
				namemap[name1] = True
			if name2 not in namemap:
				namemap[name2] = True
			if (name1, name2) in namepairs:
				namepairs[(name1, name2)] += 1
			else:
				namepairs[(name1, name2)] = 1
		for name in namemap:
			if name in names:
				names[name] += 1
			else:
				names[name] = 1
	print "--zc-- frequently appeared:"
	for e in names:
		if names[e] >= 3:
			print e + ": " + str(names[e])
	print "--zc-- frequently appeared pairs:"
	for e in namepairs:
		if namepairs[e] >= 2:
			print e[0] + " and " + e[1] + ": "  + str(namepairs[e])

if __name__ == '__main__':
	main()
