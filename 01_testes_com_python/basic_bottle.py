from bottle import route, run

@route('/')
def home():
	return "<h1>Ola!</h1>"
	
if __name__ == "__main__":
	run()
