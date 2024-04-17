import tkinter as tk
from tkinter import ttk
import psutil
import threading
import time
import widgets
from plyer import notification

class Monitor:
    def __init__(self):
        self.CPUalertCounter = 0
        self.RAMalertCounter = 0
        self.DISKalertCounter = 0
        self.stopThread = threading.Event() # evento de threading el cual se llama al cerrar la ventana
        self.monitorThread = threading.Thread(target=self.updateStats) # thread asociado al metodo updateStats
        self.monitorThread.start() # inicia el thread

    def updateStats(self):
        while not self.stopThread.is_set(): # mientras el evento "stopThread" no se settee (cerrar ventana)
            cpuUsage = psutil.cpu_percent(interval=1)
            memoryUsage = psutil.virtual_memory().percent
            diskUsage = psutil.disk_usage('C:\\').percent

            print(f"CPU Usage: {cpuUsage}%")
            print(f"Memory Usage: {memoryUsage}%")
            print(f"Disk Usage: {diskUsage}%")

            self.updateGui(cpuUsage, memoryUsage, diskUsage) # Actualizar valores en interfaz usando funcion puente
            time.sleep(1)

    def onClosing(self): # se llama al cerrar la ventana
        self.stopThread.set() # indica como "set" a stopthread, lo que hace que se detenga el bucle de updateStats (en monitorThread)
        widgets.root.destroy() # rompe la ventana

    def updateGui(self, cpuUsage, memoryUsage, diskUsage): # metodo puente entre GUI y bucle de hilo secundario
        # "ejecutar widgets.statsFrame.changeValues(cpuUsage, memoryUsage, diskUsage) lo más pronto posible en el hilo principal"
        # el 0 indica el tiempo que debe pasar para la ejecucion (por eso "lo antes posible")
        # el primer argumento es la funcion a ejecutar, y los argumentos restantes se le pasan como argumentos a la funcion a ejecutar
        widgets.root.after(0, widgets.statsFrame.changeValues, cpuUsage, memoryUsage, diskUsage)
        self.manageAlertCounters()
        self.analizeUsages(cpuUsage, memoryUsage, diskUsage)

    # define el estado del uso de los componentes y determina un color y si se debe generar una alerta
    def analizeUsages(self, cpuUsage, memoryUsage, diskUsage): 
        if cpuUsage < 51:
            widgets.root.after(0, widgets.statsFrame.changeLabelColor, "CPU Usage", "green")
        elif cpuUsage > 50 and cpuUsage < 76:
            widgets.root.after(0, widgets.statsFrame.changeLabelColor, "CPU Usage", "orange")
        else: # las condiciones para la alerta es que el contador correspondiente este en 0 y que el valor de uso sea el establecido
            widgets.root.after(0, widgets.statsFrame.changeLabelColor, "CPU Usage", "red")
            if self.CPUalertCounter == 0:
                self.makeAlert('CPU usage exceeded 75%')
                self.CPUalertCounter = 3600 # inicia contador para asegurar que esta alerta no vuelva a aparecer por 1 hora
        
        if memoryUsage < 51:
            widgets.root.after(0, widgets.statsFrame.changeLabelColor, "Memory Usage", "green")
        elif memoryUsage > 50 and memoryUsage < 76:
            widgets.root.after(0, widgets.statsFrame.changeLabelColor, "Memory Usage", "orange")
        else:
            widgets.root.after(0, widgets.statsFrame.changeLabelColor, "Memory Usage", "red")
            if self.RAMalertCounter == 0:
                self.makeAlert('Memory usage exceeded 75%')
                self.RAMalertCounter = 3600

        if diskUsage < 76:
            widgets.root.after(0, widgets.statsFrame.changeLabelColor, "Disk Usage", "green")
        elif diskUsage > 75 and diskUsage < 91:
            widgets.root.after(0, widgets.statsFrame.changeLabelColor, "Disk Usage", "orange")
        else:
            widgets.root.after(0, widgets.statsFrame.changeLabelColor, "Disk Usage", "red")
            if self.DISKalertCounter == 0:
                self.makeAlert('Disk usage exceeded 90%')
                self.DISKalertCounter = 3600

    def makeAlert(self, message):
        notification.notify(
                title='System Alert',
                message=message,
                app_icon=None,  # Ruta al archivo de ícono
                timeout=10,  # Duración de la notificación
            )
        
    def manageAlertCounters(self): 
        if self.CPUalertCounter != 0:
            self.CPUalertCounter -= 1
        if self.RAMalertCounter != 0:
            self.RAMalertCounter -= 1
        if self.DISKalertCounter != 0:
            self.DISKalertCounter -= 1

monitor = Monitor()

widgets.root.protocol("WM_DELETE_WINDOW", monitor.onClosing) # asegura que hilo secundario se detenga al cerrar ventana
widgets.root.mainloop()


