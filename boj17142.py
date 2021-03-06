from itertools import combinations
from collections import deque
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
v_lst = []
for i in range(n):
	for j in range(n):
		if mat[i][j] == 2:
			v_lst.append((i, j))


def bfs(com):
	d = [[-1] * n for _ in range(n)]
	q = deque()
	m_val = 0
	for c in com:
		d[v_lst[c][0]][v_lst[c][1]] = 0
		q.append((v_lst[c][0], v_lst[c][1]))
	while q:
		x, y = q.popleft()
		for k in range(4):
			nx, ny = x + dx[k], y + dy[k]
			if nx < 0 or n <= nx or ny < 0 or n <= ny:
				continue
			if d[nx][ny] == -1 and mat[nx][ny] != 1:
				d[nx][ny] = d[x][y] + 1
				q.append((nx, ny))
	for i in range(n):
		for j in range(n):
			if d[i][j] == -1 and mat[i][j] == 0:
				return -1
	for i in range(n):
		for j in range(n):
			if mat[i][j] != 2 and m_val < d[i][j]:
				m_val = d[i][j]
	return m_val


comb_lst = list(combinations(range(len(v_lst)), m))
ans = 2500
for com in comb_lst:
	tmp = bfs(com)
	if ans > tmp and tmp != -1:
		ans = tmp
if ans == 2500:
	print(-1)
else:
	print(ans)