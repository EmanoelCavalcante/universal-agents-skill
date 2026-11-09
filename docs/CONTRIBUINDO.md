# Como acrescentar ou alterar uma skill

1. Escolha um nome curto em kebab-case (`nome-da-skill`) e uma categoria no `CATALOGO.json`.
2. Crie `skills/nome-da-skill/SKILL.md` com YAML frontmatter (`name`, `description`) e instruções concisas.
3. Descreva quando usar, quando não usar, procedimento, limites e critérios de saída.
4. Verifique que o conteúdo seja aplicável a múltiplas IAs e não contenha detalhes privados.
5. Execute `python scripts/validate_skills.py` e `python -m unittest discover -s tests`.
6. Teste pelo menos uma tarefa real em modo Mentor/Executor/Revisor e anote o resultado em `tests/casos-manual.json`.
7. Abra PR ou commit com mensagem descritiva. Atualize `CATALOGO.json` e crie tag ao lançar versão.
