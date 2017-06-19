import requests

# Variaveis de cores
vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[1;33m'
preto = '\033[30m'
branco = '\033[37m'
original = '\033[0;0m'
reverso = '\033[2m'    
default1 = '\033[0m'

banner = '''

██╗    ██╗███████╗██████╗     ██████╗  ██╗██████╗ ██████╗  ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗    ██╗  ██╗██╗   ██╗███╗   ██╗████████╗██████╗ ██████╗ 
██║    ██║██╔════╝██╔══██╗    ██╔══██╗███║██╔══██╗╚════██╗██╔════╝╚══██╔══╝██╔═████╗██╔══██╗╚██╗ ██╔╝    ██║  ██║██║   ██║████╗  ██║╚══██╔══╝╚════██╗██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝    ██║  ██║╚██║██████╔╝ █████╔╝██║        ██║   ██║██╔██║██████╔╝ ╚████╔╝     ███████║██║   ██║██╔██╗ ██║   ██║    █████╔╝██████╔╝
██║███╗██║██╔══╝  ██╔══██╗    ██║  ██║ ██║██╔══██╗ ╚═══██╗██║        ██║   ████╔╝██║██╔══██╗  ╚██╔╝      ██╔══██║██║   ██║██║╚██╗██║   ██║    ╚═══██╗██╔══██╗
╚███╔███╔╝███████╗██████╔╝    ██████╔╝ ██║██║  ██║██████╔╝╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║       ██║  ██║╚██████╔╝██║ ╚████║   ██║   ██████╔╝██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝     ╚═════╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝

		 '''

about = '''
					+-----------------------+
					| Web D1r3ct0ry Hunt3r  |
					+-----------------------+
					|   Coder: Sr. Biggs    |
					|   Telegram: @SrBiggs  |
					|      Version: 1.0     |
					|   GitHub: BiggsCoder  |
					+-----------------------+
		'''
print(verde+banner+"\n"+default1+about+"\n")
url = input(amarelo+"Digite sua url: "+default1)
quest = input("\n"+amarelo+"Você tem uma wordlist? [Y/n]  "+default1)
if quest == 'Y':
	wordd = input("\n"+magenta+"Informe o diretorio da sua wordlist: "+default1)
	word = open(wordd)
	wrdinfo = word.readlines()
	for x in wrdinfo:
		codigo = 404
		try:
			req2 = requests.get(url+x)
			codigo = req2.status_code
		except:
			print(vermelho+"[!] Ocorreu um erro ...")
		if codigo != 404:
			print(default1+"+----------------------------------------------------------+")
			print(ciano+"|              [+]        Was found                        |")
			print(default1+"+----------------------------------------------------------+")
			print(ciano+"            URL: "+ url + x)
			print(ciano+"            Codigo: "+ str(codigo))
			print(default1+"+----------------------------------------------------------+\n")
			word.close()
			log = open('founds.txt','a+')
			log.write("[+] URL Encontrada [+]"+"\n")
			log.write("URL: "+ url + x + "\n")
			log.write("Codigo: "+str(codigo))
			log.write("\n\n")
			log.close()
		else:
			print(default1+"+----------------------------------------------------------+")
			print(vermelho+"|              [!]        Not Found                        |")
			print(default1+"+----------------------------------------------------------+")
			print(branco+"            URL: "+ url + x)
			print(branco+"            Codigo: "+ str(codigo))
			print(default1+"+----------------------------------------------------------+\n")
elif quest == 'n':
	print("\n\n"+magenta+"Usaremos nossa wordlist padrão"+"\n\n")
	default = open('default.txt', 'r')
	line = default.readlines()
	for y in line:
		codigo = 404
		try:
			req1 = requests.get(url+y)
			codigo = req1.status_code
		except:
			print(vermelho+"[!] Ocorreu um erro ...")
		if codigo != 404:
			print(default1+"+----------------------------------------------------------+")
			print(ciano+"|              [+]        Was found                        |")
			print(default1+"+----------------------------------------------------------+")
			print(ciano+"            URL: "+ url + y)
			print(ciano+"            Codigo: "+ str(codigo))
			print(default1+"+----------------------------------------------------------+\n")
			default.close()
			log = open('founds.txt','a+')
			log.write("[+] URL Encontrada [+]"+"\n")
			log.write("URL: "+ url + y + "\n")
			log.write("Codigo: "+str(codigo))
			log.write("\n\n")
			log.close()
		else:
			print(default1+"+----------------------------------------------------------+")
			print(vermelho+"|              [!]        Not Found                        |")
			print(default1+"+----------------------------------------------------------+")
			print(vermelho+"            URL: "+ url + y)
			print(vermelho+"            Codigo: "+ str(codigo))
			print(default1+"+----------------------------------------------------------+\n")