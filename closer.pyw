import Config as cfg
import time
import psutil

print("Starting closer...")
myConfig = cfg.Config()

while True:
    time.sleep(1.0)
    for programName in myConfig.programsToClose:  # Recorrer cerrables
        for process in psutil.process_iter():     # Recorrer procesos
            if programName == process.name():     # Comparar
                process.kill()                    # Matar
                print(programName, "Closed.")    # Notificar
