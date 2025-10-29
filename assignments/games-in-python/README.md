

# 📘 Assignment: Jogo da Forca (Hangman)

## 🎯 Objetivo

Construir uma versão do clássico jogo da forca em Python para praticar manipulação de strings, estruturas de repetição, condicionais e entrada do usuário.

## 📝 Tarefas

### 🛠️ Tarefa 1 — Implementar o jogo básico

#### Descrição
Implemente a lógica principal do jogo: seleção aleatória de uma palavra, entrada de palpites pelo jogador, atualização do estado do jogo e verificação de vitória/derrota.

#### Requisitos
O programa completo deve:

- Selecionar uma palavra aleatoriamente a partir de uma lista pré-definida (ex.: no `starter-code.py`).
- Mostrar o progresso atual da palavra no formato `_ _ _ _` (underscores para letras não reveladas).
- Aceitar palpites de letra do usuário e atualizar o progresso quando a letra estiver presente.
- Rastrear e exibir o número de tentativas incorretas restantes.
- Encerrar o jogo quando a palavra for completamente adivinhada (vitória) ou quando as tentativas se esgotarem (derrota).
- Exibir mensagens claras de vitória ou derrota.
- Lidar com entradas inválidas (strings vazias, múltiplas letras, caracteres não alfabéticos) e palpites já realizados.

### 🛠️ Tarefa 2 — Melhorias de interface e experiência

#### Descrição
Melhore a usabilidade do jogo deixando o jogador informado sobre o estado atual (letras já tentadas, tentativas restantes) e permita jogar novamente.

#### Requisitos

- Mostrar as letras já adivinhadas (corretas e incorretas).
- Normalizar entradas para tratar maiúsculas/minúsculas.
- Permitir que o jogador reinicie uma nova partida ao final.
- (Opcional) Adicionar um desenho simples da forca conforme as tentativas erradas.

## 🧠 Dicas e casos de borda

- Se a lista de palavras estiver vazia, mostre uma mensagem de erro e encerre graciosamente.
- Rejeite palpites não alfabéticos, espaços ou strings com mais de um caractere.
- Considere palavras com letras repetidas (ex.: "banana").
- Normalize o input (use `.lower()` ou `.upper()`) para evitar distinção entre maiúsculas e minúsculas.

## 📁 Arquivos fornecidos

- `starter-code.py` — esqueleto inicial com funções/variáveis sugeridas (palavras, contadores, funções auxiliares).
- `README.md` — este arquivo com instruções e critérios.

Se quiser, crie testes simples com `unittest` para validar funções puras (ex.: revelar_letras, verificar_vitoria).

## ▶️ Como executar

Abra um terminal e execute:

```bash
python3 starter-code.py
```

ou (dependendo do ambiente):

```bash
python starter-code.py
```

## ✨ Extras / Stretch goals

- Suporte a múltiplos níveis de dificuldade (mais/menos tentativas, palavras maiores).
- Ler lista de palavras de um arquivo `words.txt`.
- Interface simples em linha de comando com cores (ex.: usando `colorama`).

## 🧾 Critérios de avaliação

- Funcionalidade: atende todos os requisitos obrigatórios.
- Robustez: trata entradas inválidas e casos de borda.
- Experiência do usuário: mensagens claras e opção para reiniciar.
- Código limpo e comentado; preferível dividir lógica em funções testáveis.

Boa sorte — divirta-se construindo a forca! 🎯
