import tkinter as tk
from tkinter import ttk
from plyer import notification

class StatsFrame:
    def __init__(self, root):
        self.CPUalertCounter = 0
        self.RAMalertCounter = 0
        self.DISKalertCounter = 0
        self.statsFrame = tk.Frame(root)
        self.cpuUsage_Label = tk.Label(self.statsFrame, text="CPU Usage: ")
        self.memoryUsage_Label = tk.Label(self.statsFrame, text="Memory Usage: ")
        self.diskUsage_Label = tk.Label(self.statsFrame, text="Disk Usage: ")
        self.placeSelf_Widgets()
        
    def placeSelf_Widgets(self): # posicionar el Frame y las labels
        self.statsFrame.grid(row=0, column=0)
        self.cpuUsage_Label.grid(row=0, column=0, sticky="w")
        self.memoryUsage_Label.grid(row=1, column=0, sticky="w")
        self.diskUsage_Label.grid(row=2, column=0, sticky="w")
    
    def updateLabels(self, cpuUsage, memoryUsage, diskUsage):
        self.changeValues(cpuUsage, memoryUsage, diskUsage)  # Cambia el texto de las labels
        self.analyzeUsages(cpuUsage, memoryUsage, diskUsage)  # Analiza el valor y cambia el color correspondiente
        self.manageAlertCounters()  # Restar 1 a los contadores de alertas en caso de que sea necesario
        
    def changeValues(self, cpuValue, memoryValue, diskValue): # modificar los valores de los stats, modificando el texto de labels
        self.cpuUsage_Label.config(text=f"CPU Usage: {cpuValue}")
        self.memoryUsage_Label.config(text=f"Memory Usage: {memoryValue}")
        self.diskUsage_Label.config(text=f"Disk Usage: {diskValue}")

    def analyzeUsages(self, cpuUsage, memoryUsage, diskUsage): 
        if cpuUsage < 51:
            self.changeLabelColor("CPU Usage", "green")
        elif cpuUsage > 50 and cpuUsage < 76:
            self.changeLabelColor("CPU Usage", "orange")
        else: # las condiciones para la alerta es que el contador correspondiente este en 0 y que el valor de uso sea el establecido
            self.changeLabelColor("CPU Usage", "red")
            if self.CPUalertCounter == 0:
                self.makeAlert('CPU usage exceeded 75%')
                self.CPUalertCounter = 3600 # inicia contador para asegurar que esta alerta no vuelva a aparecer por 1 hora
        
        if memoryUsage < 51:
            self.changeLabelColor("Memory Usage", "green")
        elif memoryUsage > 50 and memoryUsage < 76:
            self.changeLabelColor("Memory Usage", "orange")
        else:
            self.changeLabelColor("Memory Usage", "red")
            if self.RAMalertCounter == 0:
                self.makeAlert('Memory usage exceeded 75%')
                self.RAMalertCounter = 3600

        if diskUsage < 76:
            self.changeLabelColor("Disk Usage", "green")
        elif diskUsage > 75 and diskUsage < 91:
            self.changeLabelColor("Disk Usage", "orange")
        else:
            self.changeLabelColor("Disk Usage", "red")
            if self.DISKalertCounter == 0:
                self.makeAlert('Disk usage exceeded 90%')
                self.DISKalertCounter = 3600

    def changeLabelColor(self, label, color):
        match label:
            case "CPU Usage":
                self.cpuUsage_Label.config(fg=color)
            case "Memory Usage":
                self.memoryUsage_Label.config(fg=color)
            case "Disk Usage":
                self.diskUsage_Label.config(fg=color)

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