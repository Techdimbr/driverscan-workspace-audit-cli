# 🏛️ README DE INSTRUÇÕES PRINCIPAIS — DriverScan Workspace Audit CLI

**Repositório Oficial:** `https://github.com/Techdimbr/driverscan-workspace-audit-cli`  
**Classificação:** Projeto de Referência Técnica Corporativa (Padrão Open-Core)  
**Doutrina de Engenharia:** Kether_1 · Central de Tecnologia TECHDIM  
**Status Atual:** Base Canônica Homologada — Pronto para Expansão de Funções  
**Website Institucional:** https://techdimbr.github.io/techdimbr/  
**Licença:** MIT Corporate  

---

## 1. Identificação e Propósito do Projeto
- **Nome Comercial:** DriverScan Workspace Audit CLI
- **Identificador (Slug):** `driverscan-workspace-audit-cli`
- **Categoria:** Auditoria & Governança Google Workspace
- **Stack Tecnológica:** Python 3 (stdlib puro), Google Drive API v3, SQLite3, JSON
- **Objetivo Central:** Fornecer uma ferramenta CLI ultrarrápida e determinística para inventariar arquivos e permissões de domínios corporativos Google Workspace, classificando riscos de compartilhamento público e exfiltração de dados.

### Casos de Uso Reais
1. **Auditoria Pré-M&A e Due Diligence:** Avaliação do estado de vazamento de dados de uma empresa antes de aquisição.
2. **Governança Pós-Desligamento:** Identificação de pastas corporativas com acessos concedidos a e-mails pessoais de ex-colaboradores.
3. **Varredura Preventiva de Links Abertos:** Relatório de arquivos compartilhados com a opção `Qualquer pessoa com o link pode visualizar/editar`.

---

## 2. Estrutura dos Módulos em `03_APLICACAO/src/`

```text
03_APLICACAO/src/
├── scanner.py                         # Motor principal de varredura e cálculo de risco
├── database.py                        # Camada de persistência SQLite3 com índices de pesquisa
├── reporter.py                        # Gerador de relatórios executivos em Markdown e JSON
└── credentials_helper.py              # Leitor seguro de credenciais Service Account / OAuth
```

---

## 3. Guia Operacional para o Desenvolvedor

1. **Bootstrap do Ambiente:**
   ```bash
   ./iniciar.sh
   ```
2. **Executar Testes Unitários:**
   ```bash
   python3 -m unittest discover 03_APLICACAO/tests
   ```
3. **Auditar Integridade Criptográfica dos Arquivos:**
   ```bash
   ./00_AUDITORIA/verificar_integridade.sh --gerar
   ```

---

## 4. Diretrizes e Regras de Negócio da Função (Para Preenchimento)
<!-- ÁREA DESTINADA À ESPECIFICAÇÃO DE NOVOS RECURSOS DE VARREDURA -->
- [x] Motor de pontuação de severidade de permissões (`ALTO`, `MEDIO`, `BAIXO`);
- [x] Armazenamento de resultados em tabela SQLite normalizada;
- [ ] Integração com suporte a delegação de autoridade em todo o domínio (Domain-Wide Delegation);
- [ ] Módulo de revogação automática opcional (`--revoke-public-links`) com confirmação interativa.
