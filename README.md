# Universal Agent Skills

Biblioteca versionada de **17 skills para múltiplas IAs**, escrita em português brasileiro e estruturada segundo a especificação aberta [Agent Skills](https://agentskills.io/).

## Objetivo
Ter **uma fonte canônica** para habilidades de mentoria, programação, organização, revisão e contextualização, evitando manter instruções diferentes para cada fornecedor.

| Categoria | Skills |
| --- | --- |
| Contextualização | `contexto-profissional`, `contextualizacao-de-projeto`, `pesquisa-academica-orientada` |
| Coding | `mentoria-programacao`, `backend-java-spring`, `depuracao-com-evidencias`, `implementacao-agil-controlada`, `testes-automatizados` |
| Gerência | `planejamento-tecnico`, `kanban-e-acompanhamento`, `automacoes-e-integracoes`, `documentacao-git-e-decisoes`, `comunicacao-e-prospeccao` |
| Avaliação | `revisao-critica-de-codigo`, `avaliacao-de-arquitetura`, `avaliacao-academica`, `auditoria-de-entrega` |

## Estrutura

```text
universal-agent-skills/
├── skills/                    # Fonte única: uma pasta por habilidade
│   ├── mentoria-programacao/
│   │   └── SKILL.md
│   └── ... (17)
├── adapters/                  # Modelos para AGENTS.md, CLAUDE.md, GEMINI.md
├── templates/                 # Modelos sem informações sensíveis
├── scripts/                   # Instalar, validar e empacotar
├── tests/                     # Testes do empacotamento e critérios de uso
├── docs/                      # Arquitetura, compatibilidade, segurança
├── CATALOGO.json
└── .github/workflows/validate.yml
```

## Uso rápido

Requer Python 3.10+ (stdlib, sem dependências externas).

```bash
# Verifique metadados e integridade
python scripts/validate_skills.py

# Instale as 17 skills no Claude Code para o usuário atual
python scripts/install_skills.py --agent claude --scope user

# Instale apenas uma skill no Codex em um projeto-alvo
python scripts/install_skills.py --agent codex --scope project --target /caminho/projeto --skill mentoria-programacao

# Prepare ZIP de uma skill para importação onde disponível
python scripts/package_skills.py --skill mentoria-programacao
```

No Windows, use `py -3` em lugar de `python`, se necessário. Consulte [instalação e compatibilidade](docs/COMPATIBILIDADE.md).

## Três modos de colaboração
- **Mentor:** orientar o aprendizado com pistas e perguntas, sem entregar código pronto por padrão.
- **Executor:** implementar tarefas expressamente delegadas, com cuidado, testes e alteração mínima.
- **Revisor:** avaliar e justificar achados sem editar automaticamente.

## Portabilidade
O `SKILL.md` é portátil; a **descoberta, as permissões e a aplicação das skills variam por agente**. O script instala cópias em diretórios suportados por cada ferramenta. Não execute instalações em todo projeto indiscriminadamente.

## Privacidade
Arquivos em `private/` e `local/` **não são versionados**. Os contextos específicos dos projetos do pacote anterior foram preservados **localmente** em `private/projetos/`, mas não devem ser publicados sem revisão. O pacote completo disponibilizado localmente contém esses arquivos; verifique antes de compartilhar o ZIP. Veja [PRIVACIDADE.md](docs/PRIVACIDADE.md).

## Contribuição e licença
Consulte [CONTRIBUINDO.md](docs/CONTRIBUINDO.md) e [LICENCIAMENTO.md](docs/LICENCIAMENTO.md). Nenhuma licença pública foi escolhida automaticamente.

## Documentação oficial
- https://agentskills.io/specification
- https://code.claude.com/docs/en/skills
- https://code.visualstudio.com/docs/agent-customization/agent-skills
- https://geminicli.com/docs/cli/skills/
- https://cursor.com/docs/skills
