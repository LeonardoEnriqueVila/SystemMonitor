from queue import Queue, Empty

class QueueManager:
    def __init__(self, statsFrame, root): # se obtiene root y statsFrame en init, evitando la dependencia
        self.statsFrame = statsFrame
        self.root = root
        self.queue = Queue() # crear instancia de Queque
    
    def processQueue(self):
        try:
            cpuUsage, memoryUsage, diskUsage = self.queue.get_nowait() # obtiene los valores guardados en queque
        except Empty:
            pass
        else:
            # Actualizar la GUI con los nuevos valores
            self.root.after(0, self.statsFrame.updateLabels, cpuUsage, memoryUsage, diskUsage)
        self.root.after(100, self.processQueue)  # Revisar la cola cada 100 ms -> de forma recursiva, se genera un bucle 

    def addToQueue(self, cpuUsage, memoryUsage, diskUsage):
        self.queue.put((cpuUsage, memoryUsage, diskUsage))