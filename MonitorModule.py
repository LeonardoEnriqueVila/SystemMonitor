import tkinter as tk
from tkinter import ttk
import psutil
import threading
import time

class Monitor:
    def __init__(self, queque):
        self.stopThread = threading.Event() # evento de threading el cual se llama al cerrar la ventana
        self.monitorThread = threading.Thread(target=self.updateStats) # thread asociado al metodo updateStats
        self.monitorThread.start() # inicia el thread
        self.queue = queque

    def updateStats(self):
        while not self.stopThread.is_set(): # mientras el evento "stopThread" no se settee (cerrar ventana)
            cpuUsage = psutil.cpu_percent(interval=1)
            memoryUsage = psutil.virtual_memory().percent
            diskUsage = psutil.disk_usage('C:\\').percent
            self.queue.addToQueue(cpuUsage, memoryUsage, diskUsage) # añade a la cola estos valores para usar en el hilo principal
            time.sleep(1)
    
    def onClosing(self): # se llama al cerrar la ventana
        self.stopThread.set() # indica como "set" a stopthread, lo que hace que se detenga el bucle de updateStats (en monitorThread)
        self.monitorThread.join() # esperar al thread de monitoreo para finalizar