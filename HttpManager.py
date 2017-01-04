import socket

class HttpManager
	def getByName(domainName):
		print(socket.gethostbyname(domainName))