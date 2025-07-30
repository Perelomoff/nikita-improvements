import psutil
import time
import logging

# Настройка логирования для записи данных в файл
logging.basicConfig(filename='performance.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def monitor_performance():
    try:
        # Получение информации о загрузке процессора и использования памяти
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        
        # Запись информации в лог
        logging.info(f"CPU Usage: {cpu_usage}%")
        logging.info(f"Memory Usage: {memory_info.percent}%")
    
    except Exception as e:
        logging.error(f"Ошибка при мониторинге производительности: {e}")

if __name__ == "__main__":
    while True:
        # Мониторинг каждую минуту
        monitor_performance()
        time.sleep(60)