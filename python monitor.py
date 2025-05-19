#psutil: Biblioteca python que acessa dados do sistema como memoria, cpu etc.

#time (Time-related functions): Módulo para lidar com o tempo como medir o tempo de execução,
#lidar com data e horários etc

#subprocess: Biblioteca padrao do python que permite criar e gerenciar novos processos 
#ex: Neste código é usado para rodar o comando nvidia-smi e obter informações da gpu.

#Intalar a biblioteca: pip install psutil


import psutil
import time
import subprocess

#Função para pegar informações da GPU.
def get_gpu_info():
    try:
        # Tenta obter as informações da GPU via nvidia-smi
        output = subprocess.check_output([
            "nvidia-smi", 
            "--query-gpu=utilization.gpu,memory.used,memory.total,temperature.gpu", 
            "--format=csv,noheader,nounits"
        ])
        usage, mem_used, mem_total, temp_gpu = output.decode().strip().split(", ")
        return f"GPU: {usage}% | RAM GPU: {mem_used}MiB / {mem_total}MiB | Temp: {temp_gpu}°C"
    except Exception as e:
        # Caso ocorra algum erro, retorna uma mensagem indicando que os dados da GPU estão indisponíveis
        return "GPU: Dados não disponíveis."

#Função principal para monitoramento
def monitorar():
    # Pergunta ao usuário qual processo deseja monitorar
    process_name = input("Digite o nome do arquivo .exe que deseja monitorar (exemplo: b1-Win64-Shipping.exe): ")

    log_path = "log.txt"

#Abre o arquivo de log e inicia o monitoramento
    with open(log_path, "w") as f:
        f.write("Iniciando monitoramento...\n")

    while True:
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'status', 'create_time']):
            if proc.info['name'] == process_name:
                cpu = proc.info['cpu_percent']
                mem = proc.info['memory_info'].rss / 1024 / 1024  # RAM em MB
                status = proc.info['status']
                tempo_exec = time.time() - proc.info['create_time']
                gpu_info = get_gpu_info()  # Obtém as informações da GPU

                # Exibe as informações no terminal
                print(
                    f"[{time.strftime('%H:%M:%S')}] "
                    f"Processo: {process_name} | CPU: {cpu:.1f}% | RAM: {mem:.1f}MB | "
                    f"Status: {status} | Tempo em execução: {int(tempo_exec)}s"
                )
                if gpu_info:
                    print(f"  {gpu_info}")
                else:
                    print("  GPU: Dados não disponíveis.")

                # Escreve as informações no arquivo de log
                with open(log_path, "a") as f:
                    f.write(
                        f"[{time.strftime('%H:%M:%S')}] "
                        f"Processo: {process_name} | CPU: {cpu:.1f}% | RAM: {mem:.1f}MB | "
                        f"Status: {status} | Tempo em execução: {int(tempo_exec)}s\n"
                    )
                    if gpu_info:
                        f.write(f"  {gpu_info}\n")
                    else:
                        f.write("  GPU: Dados não disponíveis.\n")
                break
        time.sleep(5)

#Executa a função de monitoramento
monitorar()