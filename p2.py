
all_m = []
x = range(1000)
for i in x:
	if i % 3 == 0:
		m_3 = i
	if m_3 not in all_m:
		all_m.append(m_3)
for i in x:
	if i % 5 == 0:
		m_5 = i
	if m_5 not in all_m:
		all_m.append(m_5)
all_m.sort()
sum_multiples = sum(all_m)
print(sum_multiples)
