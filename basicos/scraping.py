from urllib.request import urlopen
with urlopen('https://formacion.ipartek.com/cursos/buscar.asp?op=t&b=&modalidad=-1') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if 'python' in line:
            print(line.strip())