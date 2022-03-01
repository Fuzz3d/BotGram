import sys
import time
from instabot import Bot

print("[*] En caso de fallar el programa, eliminar la carpeta config y volver a correr el script. :)")
time.sleep(3)
bot = Bot()
bot.login()


def menu():
    print('''
       }--------------{+} Coded By Fuzzed {+}--------------{
       }--------{+}  github.com/Fuzz3d {+}--------{
    ''' '''
       {1}--Subir foto
       {2}--Guardar Stats de un usuario 
       {3}--Descargar fotos de un usuario
       {4}--Obtener seguidores de un usuario (ID)
       {5}--Borrar todas tus fotos
       {6}--Dejar de seguir usuarios que no te siguen 
       {7}--Enviar un mensaje
       {8}--Dejar de seguir a todos :)
       {99}-SALIR\n
     '''
)
    
menu()
option = int(input("        Escoja una opcion: "))
   
def subir_foto():
    
    foto = input("Ruta de la foto: ")
    descripcion = input("Descripcion de la foto: ")
    bot.upload_photo(foto,caption=descripcion)

def stats():

    target = input("Ingrese su objetivo: ")
    bot.save_user_stats(target)
    menu()

def descargar_fotos():

    objetivo = input("Target: ")

    medias = bot.get_total_user_medias(objetivo)
    bot.download_photos(medias)

def obtener_seguidores():

    username = input("Usuario: ")
    followers = bot.get_user_followers(username)
    for follower in followers:
        print(follower)

def borrar_fotos():

    medias = bot.get_total_user_medias(bot.user_id)
    bot.delete_medias(medias)

def unfollow_non_followers():

    bot.unfollow_non_followers

def enviar_mensaje():

    mensaje = input("Mensaje: ")
    usuario = input("Ingrese un usuario o mas. (Separados por coma): ")
    bot.send_message(mensaje,[usuario])

def unfollow():

    bot.unfollow_everyone()

def exit():
    sys.exit()

while option !=0:
    if option == 1:
        subir_foto()
    elif option == 2:
        stats()
    elif option == 3:
        descargar_fotos()
    elif option == 4:
        obtener_seguidores()
    elif option == 5:
        borrar_fotos()
    elif option == 6:
        unfollow_non_followers()
    elif option == 7:
        enviar_mensaje()
    elif option == 8:
        unfollow()
    elif option == 99:
        print("Gracias por usar este programa, que tengas un buen dia :)") 
        exit()
    else:
        print("Opcion invalida... ")  
    
    menu()
  

   
