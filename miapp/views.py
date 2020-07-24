from django.shortcuts import render,HttpResponse, redirect

# Create your views here.
#  CREANDO PRIMER METODO 

layout="""
	<h1> Pro¿yecto web</h1>
	<hr/>
	<ul>
		<li>
			<a href="/inicio"> Inicio</a>
		</li>
		<li>
			<a href="/saludo"> Mensaje</a>
		</li>
		<li>
			<a href="/rango"> Monstar los numeros </a>
		</li>
		</hr>
	"""



def saludo(request):

	return render(request,'saludo.html')

def index(request):
	
	return render(request, 'index.html')	
     
def rango(request):
	a=10
	b=20
	resultado = f"""
				<h3> numeros [{a},{b}]</h3>
				resultado: <br>
				<ul>
	"""
	while a<=b:
		resultado += f"<li>{a}<li>"
		a+=1
	resultado +="</ul>"
	return HttpResponse(layout + resultado)

def rango2(request,a=0,b=100):
	if a>b:
		return redirect('rango2',a=b,b=a)
	resultado = f"""
				<h3> numeros [{a},{b}]</h3>
				resultado: <br>
				<ul>
	"""
	while a<=b:
		resultado += f"<li>{a}<li>"
		a+=1
	resultado +="</ul>"
	return HttpResponse(layout + resultado)