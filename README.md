# Informações RouterOS

Script Python simples para extrair informações de versão e modelo de arquivos de configuração RouterOS e exportar para CSV.

## 📋 Descrição

Este script processa múltiplos arquivos de configuração do RouterOS e extrai automaticamente:
- Nome do arquivo
- Versão do RouterOS
- Modelo do router

Os dados são salvos em um arquivo CSV para fácil análise e gerenciamento de inventário.

## 🔧 Requisitos

- Python 3.6 ou superior
- Nenhuma dependência externa (usa apenas bibliotecas padrão)

## 📦 Instalação

1. Clone ou faça download deste repositório:
```bash
git clone git@github.com:BatistaFelipe/mk_routers_info.git
cd mk_routers_info
```

2. Pronto! Não há dependências para instalar.

## 🚀 Como Usar

### Uso Básico

1. Coloque seus arquivos de configuração RouterOS em um diretório
2. Execute o script:

```bash
python run.py
```

### Exemplo de Arquivo de Entrada
```
# nov/11/2025 14:14:02 by RouterOS 6.49.9
# software id = XXXXXX
#
# model = RB941-2nD
# serial number = XXXXXXXX
```

### Exemplo de Saída (CSV)

```csv
nome_arquivo,versao_routeros,modelo_router
router_filial1.rsc,6.49.9,RB941-2nD
router_filial2.rsc,6.50.1,RB750Gr3
router_matriz.rsc,7.1.5,CCR1036-12G-4S
```

## 📁 Estrutura do Projeto

```
mk_routers_info/
├── run.py                  # Script principal
├── rsc/                    # Coloque seus arquivos aqui
├── routers_info.csv        # Arquivo de saída gerado
└── README.md               # Este arquivo
```

## 💡 Exemplos de Uso

### Processar arquivos do diretório atual
```python
processar_arquivos(".", "inventario_routers.csv")
```

### Processar arquivos de uma pasta específica
```python
processar_arquivos("/backup/configs/routeros", "routers_2025.csv")
```

## 📝 Formato dos Arquivos

O script espera que os arquivos tenham as seguintes linhas no início:
- Linha com `by RouterOS X.XX.X` para extrair a versão
- Linha com `# model = MODELO` para extrair o modelo

## 👤 Autor

Este projeto foi criado por **Claude Sonnet 4.5** (Anthropic) em dezembro de 2025.

Desenvolvido como uma solução para automatizar a extração de informações de configurações RouterOS.

## 🔗 Links Úteis

- [Documentação RouterOS](https://wiki.mikrotik.com/wiki/Manual:TOC)
- [Python Documentation](https://docs.python.org/3/)

---

⭐ Se este projeto foi útil para você, considere dar uma estrela!