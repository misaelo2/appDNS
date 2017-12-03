import sys
import subprocess
#EJECUTAR SCRIPT COMO ROOT

archivo=open("/var/cache/bind/misael.iesgn.org","a+")

#SI PULSAMOS -A ,AÑADIMOS 
if sys.argv[1] == "-a" :
#PARA AÑADIR DIRECCIONES
	if sys.argv[2]=="-dir" :
		archivo.write(sys.argv[3]+"	IN	A	"+str(sys.argv[4])+"\n")
		#MODIFICAMOS LA ZONA INVERSA , AÑADIENDO AL FINAL 
		if "10.0.0" in  sys.argv[4] :
			archivo2=open("/var/cache/bind/10.0.0.in-addr.arpa","a+")
			archivo2.write(sys.argv[4].split(".")[3]+"	IN	PTR	"+sys.argv[3]+".misael.gonzalonazareno.org."+"\n") 
			archivo2.close()
		#MODIFICAMOS LA ZONA INVERSA , AÑADIENDO AL FINAL 
		elif "172.22" in sys.argv[4] :
			archivo2=open("/var/cache/bind/172.22.in-addr.arpa ","a+")
			archivo2.write(sys.argv[4].split(".")[3]+"."+sys.argv[4].split(".")[2]+"	IN	PTR	"+sys.argv[3]+".misael.gonzalonazareno.org."+"\n") 
			archivo2.close()
#PARA AÑADIR ALIASES
	elif sys.argv[2]=="-alias" :
		archivo.write(sys.argv[3]+"	IN	CNAME	"+str(sys.argv[4])+"\n") 
	else:
		print ("error en argumentos")



#SI PULSABOS -B , ELIMINAMOS
if sys.argv[1] =="-b" :
	lista=archivo.readlines()
	archivo.close()
	archivo=open("/var/cache/bind/misael.iesgn.org","w")
	for elem in lista :
		if sys.argv[2] not in elem :
			archivo.write(elem)
	archivo.close()


subprocess.call('systemctl restart bind9', shell=True)
