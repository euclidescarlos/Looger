# 🤖 Monitor Logger

Um monitor de processos em Python desenvolvido para a cadeira de **Arquitetura e Organização de Computadores** do 3º período do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O software coleta dados de desempenho de aplicativos em execução e os registra em um arquivo de log, enquanto exibe as informações em tempo real no terminal.

## 📚Contexto Acadêmico

Este projeto foi desenvolvido como trabalho prático para a disciplina de Arquitetura e Organização de Computadores, com os seguintes objetivos:

- Demonstrar na prática os conceitos de monitoramento de recursos de hardware
- Analisar o consumo de componentes como CPU, RAM e GPU
- Implementar uma solução que interage diretamente com o sistema operacional

## ⚙️Funcionalidades

- Monitora o uso de CPU e RAM de qualquer processo em execução
- Coleta dados da GPU NVIDIA (quando disponível) incluindo:
  - Utilização da GPU
  - Uso de memória da placa de vídeo
  - Temperatura da GPU
- Exibe informações em tempo real no terminal
- Armazena todos os dados em um arquivo `log.txt`
- Interface simples onde o usuário informa qual processo deseja monitorar

## 📋Requisitos

- Python 3.x
- Biblioteca psutil (`pip install psutil`)
- Drivers NVIDIA instalados (para monitoramento da GPU)
- Utilitário `nvidia-smi` (vem com os drivers NVIDIA)

## 🚀Como Usar

1. Clone o repositório ou baixe o arquivo `monitor.py`
2. Execute o script com Python: python monitor.py
3. Quando solicitado, digite o nome do arquivo .exe do processo que deseja monitorar (ex: `Discord.exe`)
4. O monitor começará a exibir as informações no terminal e salvá-las no arquivo `log.txt`

## 📊Dados Coletados

**Para o processo monitorado:**
- Nome do processo
- Uso de CPU (%)
- Uso de RAM (MB)
- Status (running, sleeping, etc)
- Tempo de execução (segundos)

**Para a GPU NVIDIA (quando disponível):**
- Utilização da GPU (%)
- Memória usada/total (MiB)
- Temperatura (°C)

## 💻Exemplo de Saída
`[22:15:52] Processo: Discord.exe | CPU: 0.0% | RAM: 549.9MB | Status: running | Tempo em execução: 9809s
GPU: 0% | RAM GPU: 87MiB / 4096MiB | Temp: 58°C`

## ⚙️Personalização

O intervalo de atualização padrão é de 5 segundos. Para alterar, modifique o valor em `time.sleep(5)` no código.

## ⚠️Limitações

- O monitoramento da GPU só funciona com placas NVIDIA
- Requer permissões para acessar informações do sistema
- O nome do processo deve ser exato (incluindo .exe)

## 👨‍💻Autor

Projeto desenvolvido por Euclides Neto, Eduardo Henrique e Gabriel Teixeira como parte das atividades acadêmicas do curso de ADS.
