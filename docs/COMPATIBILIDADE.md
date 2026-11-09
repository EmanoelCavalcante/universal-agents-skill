# Instalação por agente

A biblioteca guarda as skills em `skills/<nome>/SKILL.md`. O instalador **copia** cada diretório para o local escolhido; não cria links simbólicos e não substitui arquivos existentes sem `--force`.

| Agente | Diretório do projeto | Diretório pessoal |
| --- | --- | --- |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| OpenAI Codex | `.agents/skills/` | `~/.agents/skills/` |
| Gemini CLI | `.gemini/skills/` | `~/.gemini/skills/` |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` |
| GitHub Copilot | `.github/skills/` | `~/.copilot/skills/` |

> Algumas ferramentas também reconhecem caminhos alternativos, como `.agents/skills/`. A tabela mostra os destinos explícitos escolhidos por este projeto, não a lista completa de aliases.

## Exemplos

```bash
python scripts/validate_skills.py
python scripts/install_skills.py --agent claude --scope user
python scripts/install_skills.py --agent all --scope project --target /caminho/projeto --skill revisao-critica-de-codigo
python scripts/package_skills.py --skill revisao-critica-de-codigo
```

### Claude no navegador e outras interfaces de upload
Não lê automaticamente arquivos da sua máquina ou do GitHub apenas porque existem. Gere um ZIP por skill e importe manualmente na interface que suporta skills.

### ChatGPT/Codex
O Codex usa skills locais em `.agents/skills/`. O suporte da interface ChatGPT depende dos recursos de skills disponíveis para a conta/ambiente; instalação no Codex não transfere arquivos automaticamente para o ChatGPT web.

### Instruções gerais persistentes
Copie `adapters/AGENTS.md` para `AGENTS.md` no projeto Codex/compatíveis; `adapters/CLAUDE.md` para `CLAUDE.md` (Claude Code); `adapters/GEMINI.md` para `GEMINI.md` (Gemini CLI). Adapte às decisões concretas do projeto.

## Fontes
- https://agentskills.io/specification
- https://code.claude.com/docs/en/skills
- https://code.visualstudio.com/docs/agent-customization/agent-skills
- https://geminicli.com/docs/cli/skills/
- https://cursor.com/help/customization/skills
- https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
