resposta = int(input("Por favor, entre com o número de segundos que deseja converter:"))

dias = resposta // 86400
segundos_hora = resposta % 86400
horas = segundos_hora // 3600
segundos_minutos = segundos_hora % 3600
minutos = segundos_minutos // 60
segundos = segundos_minutos % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")