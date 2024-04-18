import tkinter as tk
import MonitorModule
import StatsFrameManager
import quequeManager

def main():
    root = tk.Tk()
    statsFrame = StatsFrameManager.StatsFrame(root)
    queue = quequeManager.QueueManager(statsFrame, root)
    monitor = MonitorModule.Monitor(queue)
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, monitor))
    queue.processQueue()
    root.mainloop()

def on_closing(root, monitor):
    monitor.onClosing()
    root.destroy()

if __name__ == "__main__":
    main()
