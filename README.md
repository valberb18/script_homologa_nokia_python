Com objetivo de deixar a homologação de ONUs nokia mais facil desenvolvi esse script.
Para homologar esse equipamento era necessario ultlizar os comandos:

-configure equipament ont interface 1/1/1/16/1 admin state down
-show pon unprovision-onu
-configure equipament ont interface 1/1/1/16/1 sernum ALCL:B67DGUZS admin-state up

Agora para facilitar é so escolher uma das opções presentes no script para realizar as tarefas
Para a construção desse script foram usadas as bibliotecas Netmiko(usada para fazer coneções 
atraves do protocolo SSH) e a biblioteca PyInstaller(usada para criar um arquivo executável a
partir de um arquivo Python ).

Essa é apenas a primeira versão desse codigo, pretendo para o futuro acresentar outras 
funcionalidades para mesma.
