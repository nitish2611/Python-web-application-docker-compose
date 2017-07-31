from flask import Flask, request
from redis import Redis
import logging
from logging.handlers import RotatingFileHandler
import time


app = Flask(__name__)
#Connecting to Redis container on default port 6379
redis = Redis(host='redis', port=6379)

#Configuring application route
@app.route('/', strict_slashes=False)
def hello():
	try:
		ip = request.remote_addr 						#Capture requester IP
		redis.ping() 								#Check if redis service is running
		redis.set('key', 'Hello World this is from redis server')
		text = redis.get('key')
		app.logger.info('ip : {0}, Message : {1}, Status: {2}'.format(ip,"Success",200)) #Log the success message
		return text
	except Exception as e:
		app.logger.error('ip : {0} , Exception : {1}'.format(ip,e), exc_info = True) #Log server exception
		return '500 SERVER ERROR. Error logged into redis.log file\n'

@app.route('/<path:dummy>')
def fallback(dummy):
    return 'Requested URL not found... Please enter valid URL\n'

if __name__ == "__main__":
    formatter = logging.Formatter(
        "%(asctime)s | %(name)-12s | %(pathname)s : %(lineno)d | %(levelname)s | %(message)s") 	#Required log format
    info_handler = RotatingFileHandler('redis.log', maxBytes=100000, backupCount=1) 	#Creation of log file  
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)
    app.logger.addHandler(info_handler)
    app.run(host="0.0.0.0", port=8080, debug=True) 		#Run the application open for all public IP's
