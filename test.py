from kodemon import kodemon

@kodemon
def counter100():
	i = 0
	while i < 10:
		print (i)
		i+=1


counter100()
