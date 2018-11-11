from django.shortcuts import render
import urllib.request
from django.http import HttpResponse
import json
import os
import sys

def index(request):
	return render(request, 'search/search.html')

def result(request):
	search_word = request.GET.get('words')
	client_id = "YOUR_CLIENT_ID"
	client_secret = "YOUR_CLIENT_SECRET"
	encText = urllib.parse.quote(search_word)
	url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
	# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
	request = urllib.request.Request(url)
	request.add_header("X-Naver-Client-Id",client_id)
	request.add_header("X-Naver-Client-Secret",client_secret)
	response = urllib.request.urlopen(request)
	rescode = response.getcode()
	if(rescode==200):
		response_body = response.read()
		result = json.loads(response_body.decode('utf-8')).get('items')
		items = results.get("search_word")
		context = {
		    	"search_word" : result
		}
		return render(request, 'search/result.html', context)
	else:
		print("Error Code:" + rescode)
