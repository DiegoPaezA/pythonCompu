import os 

print "hola"

directorioOriginal = os.getcwd()
directorio = os.path.join(os.pardir, 'directorios/miNuevoDir1')
if not os.path.isdir(directorio):
    os.mkdir(directorio)
os.chdir(directorio)

os.chdir(directorioOriginal) # vuelve al directorio inicial
os.chdir(os.environ['HOME']) # cambia al directorio home
