# 4. Elabore o algoritmo: Baseado no conhecimento adquirido nesta aula e na leitura complementar, construa o fluxograma e pseudocódigo - Utilize os passos para ir para a escola.


# Pseudocódigo
```
INÍCIO
    // Definição de variáveis
    DECLARE saldo, quantia, senha COMO INTEIRO

    ESCREVER "Ir até um Banco 24 horas"
    ESCREVER "Inserir o cartão"
    ESCREVER "Digite sua senha:"
    LER senha
    ESCREVER "Retirar o cartão"
    ESCREVER "Escolher a opção de saque"
    ESCREVER "Digite a quantia desejada:"
    LER quantia

    // Simulando um saldo existente
    saldo <- 500

    SE saldo >= quantia ENTÃO
        saldo <- saldo - quantia
        ESCREVER "Saque realizado com sucesso"
    SENÃO
        ESCREVER "Impossível realizar saque: saldo insuficiente"
    FIMSE

    ESCREVER "Sair do Banco 24 horas"

FIM
```

# Fluxograma
```
    A[Início] --> B[Ir até um Banco 24 horas]
    B --> C[Inserir o cartão]
    C --> D[Digite sua senha]
    D --> E[Retirar o cartão]
    E --> F[Escolher a opção de saque]
    F --> G[Digite a quantia desejada]
    G --> H{Saldo >= quantia?}
    H -- Sim --> I[Saque realizado com sucesso]
    H -- Não --> J[Mostrar mensagem de saldo insuficiente]
    I --> K[Sair do Banco 24 horas]
    J --> K
    K --> L[Fim]
```