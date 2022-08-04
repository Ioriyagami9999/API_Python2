from fastapi import FastAPI
import json
import requests

app= FastAPI()



@app.get('/API')
def get_api():
	res= requests.get('https://kx21dtq092.execute-api.us-east-1.amazonaws.com/Prueba/obtenerLambda')	
	v=res.json()
	return v
