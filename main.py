from config import ruta_descargas_origen, ruta_organizador_destino, extensiones_Archivos
from pathlib import Path
from datetime import datetime

import os
import shutil 

class organizador:
    """
    Clase para poder organizador archivos de un categoria especifica ("config.py") hacia una carpeta.
    """

    def __init__(self, ruta_origen:str, ruta_destino:str) -> None:
        """
        Primero comenzamos asignamos cada ruta una variable para la clase.

        Args:
            - ruta_origen (str): Ruta de la carpeta de descargas.
            - ruta_destino (str): Ruta de la carpeta de organizacion de archivos.
        """
        self.ruta_origen = Path(ruta_origen)
        self.ruta_destino = Path(ruta_destino)
        self.ruta_log = Path(ruta_destino) / "historial.log"
        self.creacion_subdirectorios = True

        self._creacion_carpetas()
    
    def _creacion_carpetas(self) -> None:
        """
        La segunda función SOLO servira crear carpetas y subcarpeta para la organizacionde archivos.
        """
                
        """ Creacion de directorio padre `Organizador` """
        if not self.ruta_destino.exists(): # En caso de que no existe la carpeta "Organizador", se creara.
            self.ruta_destino.mkdir(parents=False, exist_ok=True)
            self._registro_log("INFO", f"Creacion la carpeta {self.ruta_destino}") # Registro en log
        else:
            self._registro_log("ERROR", f"Error al tratar de crear la carpeta porque ya existe {self.ruta_destino}") # Registro en log

                
        """ Creacion de subdirectorios para guardar cada archivo """
        for sub_directorio in extensiones_Archivos.keys():
            ruta_sub_directorio = Path(ruta_organizador_destino) / sub_directorio
             
            if not ruta_sub_directorio.exists(): # Veficamos la exitencia de los directorios
                ruta_sub_directorio.mkdir(parents=False, exist_ok=True) # Creamos el directorio.
                self._registro_log("INFO", f"Creacion del subdirectorio {ruta_sub_directorio.name}") # Registro en log
            else:
                self._registro_log("ERROR", f"Error al tratar de crear el subdirectorio {ruta_sub_directorio.name}") 

        self._organizar_archivos()  # Ejecutamos el tercer paso de reorganizar archivos

    def _organizar_archivos(self):
        lista_de_archivos_descargas = [archivo for archivo in self.ruta_origen.iterdir() if archivo.is_file()]
        
        for categoria in extensiones_Archivos.keys():
            for archivo in lista_de_archivos_descargas:
                if archivo.suffix in extensiones_Archivos[categoria]:
                    shutil.move(archivo, self.ruta_destino / categoria)
                    self._registro_log("INFO", f"Se copio el archivo {archivo.name} a la carpeta {categoria}")

    def _registro_log(self, tipo, accion):
        """ Creacion de archivo log """
        if not self.ruta_log.exists():
            self.ruta_log.touch()

        with open(self.ruta_log, "a") as log: 
            log.write(f"- {datetime.now().strftime("%d/%m/%Y %H:%M")} {tipo} {accion} \n")

if __name__ == "__main__":
    organizacion = organizador(ruta_descargas_origen, ruta_organizador_destino)
