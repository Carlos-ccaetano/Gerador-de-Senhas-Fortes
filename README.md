# Gerador de Senhas Fortes

Este é um script Python simples para gerar senhas fortes e seguras com base em critérios definidos pelo usuário. Ele permite especificar o comprimento da senha e incluir ou excluir letras maiúsculas, números e símbolos. Opcionalmente, as senhas geradas podem ser salvas em um arquivo CSV.

## Funcionalidades

- Geração de senhas com comprimento personalizável.
- Opções para incluir/excluir letras maiúsculas, números e símbolos.
- Salvamento opcional da senha gerada em um arquivo `.csv` para referência futura.

## Como Usar

1. **Pré-requisitos:**
   Certifique-se de ter o Python 3 instalado em seu sistema.

2. **Execução:**
   Navegue até o diretório `gerador_senhas` no seu terminal e execute o script:
   ```bash
   python3 password_generator.py
   ```

3. **Interação:**
   O script solicitará as seguintes informações:
   - Comprimento da senha (padrão: 12)
   - Incluir letras maiúsculas? (s/n, padrão: s)
   - Incluir números? (s/n, padrão: s)
   - Incluir símbolos? (s/n, padrão: s)
   - Salvar senha em `passwords.csv`? (s/n, padrão: s)

## Exemplo de Uso

```
Gerador de Senhas Fortes
Comprimento da senha (padrão: 12): 16
Incluir letras maiúsculas? (s/n, padrão: s): s
Incluir números? (s/n, padrão: s): s
Incluir símbolos? (s/n, padrão: s): s
Senha gerada: Ex@mPl3S3nh@F0rt3
Salvar senha em 'passwords.csv'? (s/n, padrão: s): s
Senha salva com sucesso em 'passwords.csv'.
```

## Estrutura do Projeto

```
.|
├── password_generator.py
└── README.md
```

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades. Abra uma issue ou envie um pull request.


