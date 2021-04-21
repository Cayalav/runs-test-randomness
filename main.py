import random
import math
import statistics


def runsTest(l, l_median):
	runs, n1, n2 = 0, 0, 0
	# Verificación para iniciar nueva corrida
	for i in range(len(l)):
		# no. de corridas
		if (l[i] >= l_median and l[i-1] < l_median) or \
				(l[i] < l_median and l[i-1] >= l_median):
			runs += 1
		# no. valores positivos
		if(l[i]) >= l_median:
			n1 += 1
		# no. valores negativos
		else:
			n2 += 1
	runs_exp = ((2*n1*n2)/(n1+n2))+1
	stan_dev = math.sqrt((2*n1*n2*(2*n1*n2-n1-n2))/ \
					(((n1+n2)**2)*(n1+n2-1)))
	z = (runs-runs_exp)/stan_dev
	return z
	
# Generamos 100 numeros random
l = []
for i in range(100):
	l.append(random.random())
l_median= statistics.median(l)
Z = abs(runsTest(l, l_median))
print('Z-statistic= ', Z)
