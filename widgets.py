import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("System Monitor")

class StatsFrame:
    def __init__(self):
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

    def changeValues(self, cpuValue, memoryValue, diskValue): # modificar los valores de los stats, modificando el texto de labels
        self.cpuUsage_Label.config(text=f"CPU Usage: {cpuValue}")
        self.memoryUsage_Label.config(text=f"Memory Usage: {memoryValue}")
        self.diskUsage_Label.config(text=f"Disk Usage: {diskValue}")

    def changeLabelColor(self, label, color):
        match label:
            case "CPU Usage":
                self.cpuUsage_Label.config(fg=color)
            case "Memory Usage":
                self.memoryUsage_Label.config(fg=color)
            case "Disk Usage":
                self.diskUsage_Label.config(fg=color)

statsFrame = StatsFrame()




