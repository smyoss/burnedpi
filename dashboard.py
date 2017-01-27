import psutil 
p = psutil

def mem():
	mem = p.virtual_memory().percent
	return mem

def processor():
	processor = p.cpu_percent(interval=1)
	return processor