# 4. Elabore o algoritmo: Baseado no conhecimento adquirido nesta aula e na leitura complementar, construa o fluxograma e pseudocódigo - Utilize os passos para ir para a escola.


# Pseudocódigo
```
INÍCIO

    // Definição de variáveis
    ESCREVER "Passos para ir para a escola"
    ESCREVER "Acordar cedo"
    ESCREVER "Ir ao banheiro"
    ESCREVER "Abrir o armário e escolher uma roupa"
    
    ESCREVER "O tempo está quente? (S/N)"
    LER tempoQuente

    SE tempoQuente = "S" ENTÃO
        ESCREVER "Pegar uma camiseta e uma calça jeans"
    SENÃO
        ESCREVER "Pegar um agasalho e uma calça jeans"
    FIMSE

    ESCREVER "Vestir a roupa escolhida"
    ESCREVER "Tomar café"
    ESCREVER "Pegar uma condução"
    ESCREVER "Descer próximo à escola"

FIM
```

# Fluxograma
```
flowchart TD
    A[Início] --> B[Acordar cedo]
    B --> C[Ir ao banheiro]
    C --> D[Abrir o armário e escolher uma roupa]
    D --> E{O tempo está quente?}
    E -- Sim --> F[Pegar uma camiseta e uma calça jeans]
    E -- Não --> G[Pegar um agasalho e uma calça jeans]
    F --> H[Vestir a roupa escolhida]
    G --> H
    H --> I[Tomar café]
    I --> J[Pegar uma condução]
    J --> K[Descer próximo à escola]
    K --> L[Fim]
```
# Explicação do Fluxograma
1. **Início**: O algoritmo começa aqui.
2. **Acordar cedo**: O primeiro passo é acordar cedo.
3. **Ir ao banheiro**: O segundo passo é ir ao banheiro.

4. **Abrir o armário e escolher uma roupa**: O terceiro passo é abrir o armário e escolher uma roupa.
5. **O tempo está quente?**: O quarto passo é verificar se o tempo está quente.
6. **Pegar uma camiseta e uma calça jeans**: Se o tempo estiver quente, o próximo passo é pegar uma camiseta e uma calça jeans.
7. **Pegar um agasalho e uma calça jeans**: Se o tempo não estiver quente, o próximo passo é pegar um agasalho e uma calça jeans.
8. **Vestir a roupa escolhida**: O próximo passo é vestir a roupa escolhida.
9. **Tomar café**: O próximo passo é tomar café.
10. **Pegar uma condução**: O próximo passo é pegar uma condução.
11. **Descer próximo à escola**: O próximo passo é descer próximo à escola.
12. **Fim**: O algoritmo termina aqui.
```
# Observações
- O algoritmo é uma sequência de passos que descrevem como ir para a escola.
- O fluxograma é uma representação visual do algoritmo, onde cada passo é representado por um bloco e as decisões são representadas por losangos.
- O pseudocódigo é uma representação textual do algoritmo, onde cada passo é descrito em linguagem natural.
- O algoritmo pode ser adaptado para incluir mais passos ou condições, dependendo das necessidades do usuário.
- O fluxograma e o pseudocódigo são ferramentas úteis para planejar e organizar o pensamento antes de escrever o código em uma linguagem de programação específica.