from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html',{'hi':'how are u ?'})

def eggs(request):
	return HttpResponse('<h1>How many eggs u want ?</h1>')
	
def about(request):
	return render(request, 'about.html')

def count(request):
	
	fulltext = request.GET['fulltext']
	value = fulltext.split()
	print(value)
	dic = {}
	for i in value:
		if i not in dic.keys():
			dic[i] = 1
		else:
			dic[i]+=1
	print(dic)
	sorted_value = sorted(dic.items(), key = lambda x:x[1], reverse = True)
	print(sorted_value[0][0])
	return render(request, 'count.html', {'fulltext':fulltext, 'value':len(value),'max_val': sorted_value} )