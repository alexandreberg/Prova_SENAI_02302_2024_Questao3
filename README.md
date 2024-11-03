# Prova_SENAI_02302_2024_Questao3
Aqui encontram-se os arquivos referentes a Questão 3 da PROVA PRATICA - Processo Seletivo 02302/2024 - Pesquisador I - Software Embarcado

## Enunciado:
Avaliação prática:

O estudo de caso pode ser realizado em sistemas Linux ou Windows. As questões 2 e 3 devem abordar a ferramenta de versionamento git [1] e serem armazenadas em um repositório público (por exemplo, GitHub, Gitlab).

***
### Questão 3: (COM GIT)

Para o uso de sistemas embarcados, considerando entregas de protótipos e produtos, é de fundamental importância agregar funcionalidades de segurança para que o sistema não sofra com hackers, invasões e interceptação de dados. Diante disso, o padrão de criptografia avançada – ou simplesmente AES – é uma abordagem comumente utilizada em aplicações embarcadas, assim como considerado em [4].

Com um outro viés de segurança, agora considerando a abordagem de funcionalidade de código e sua robustez, uma importante abordagem é o uso de testes unitários, consistindo na verificação do comportamento de módulos de um determinado software [5].

A partir das informações, considere os caracteres a seguir:

```
a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20
```

Eles representam uma frase codificada com o algoritmo **AES**, em modo **ECB**, com tamanho de chave de 128 bits. A chave utilizada para codificar a mensagem é: **"thisisasecretkey".**

Com base no sistema de criptografia AES e aplicação de testes unitários, pede-se:

***
#### Pergunta 1.
Implemente um código em linguagem **C**, **C++**, ou **Python**, capaz de realizar a decodificação da mensagem e imprimir a mesma em terminal de execução do software:

Abaixo seguem o código comentado de resposta da pergunta 1, bem como o log de execução do código, mostrando a resposta da chave descriptografada.  
Para essa resolução foram escolhidos códigos em linguagem **python**.  

* [Código de resposta da pergunta 1](https://github.com/alexandreberg/Prova_SENAI_02302_2024_Questao3/blob/main/python/pergunta_1.py)
* [Log da execução do código pergunta 1](https://github.com/alexandreberg/Prova_SENAI_02302_2024_Questao3/blob/main/python/pergunta1_resultado.log)
* A mensagem descriptografada é:  ***Sistemas Embarcados***

***
#### Pergunta 2.
Implemente testes unitários para validar o funcionamento do código desenvolvido:

Abaixo seguem o código comentado de resposta da pergunta 2, bem como o log de execução do código, mostrando o resultado do teste unitário.

* [Código de resposta da pergunta 2](https://github.com/alexandreberg/Prova_SENAI_02302_2024_Questao3/blob/main/python/unittest/test_pergunta2.py)
* [Log da execução do código pergunta 2](https://github.com/alexandreberg/Prova_SENAI_02302_2024_Questao3/blob/main/python/unittest/test_pergunta2_resultados.log)


***
### Referências

[1] Git. Distributed even if your workflow isnt. Disponível em: <https://git-scm.com/>.  
[2] ROS. Robot Operating System. Disponível em: <https://www.ros.org/>.  
[3] Docker. Accelerate how you build, share and run applications. Disponível em: <https://www.docker.com/>.  
[4] Molcut, A. I.; Lica, S.; Lie, Ion. Cybersecurity for Embedded Systems: A review. 2022 International Symposium on Electronics and Telecommunication. DOI: 10.1109/ISETC56213.2022.10009944.  
[5] Krishnan, P.; Suman, V. Effectiveness of Random Testing of Embedded Systems. 2012 45th Hawaii International Conference on System Sciences. DOI 10.1109/HICSS.2012.233.  

***
## Estrutura de arquivos no GitHub:
```   
C:.
│   Prova_SENAI_02302_2024_Questao3.code-workspace  # Workspace para acesso direto pelo VScode
│   README.md                                       # Esse arquivo                                    
└───python                                          # Diretório para os códigos python
    │   pergunta1_resultado.log                     # Log da resposta da pergunta 1 com o código descriptografado
    │   pergunta_1.py                               # Código python da pergunta 1
    ├───unittest                                    # Diretório para os testes unificados
        │   test_pergunta2.py                       # Código do teste unificado da pergunta 2
        └───test_pergunta2_resultados.log           # Log com o resultado do teste unificado

```
