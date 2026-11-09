# Como publicar no GitHub (manual)

## Antes de publicar
1. Abra `README.md` e faça ajustes de apresentação.
2. Inspecione `docs/PRIVACIDADE.md` e o conteúdo da pasta `private/` (não é versionada).
3. Escolha uma licença conscientemente (consulte `docs/LICENCIAMENTO.md`).

## No GitHub
Crie um repositório **vazio** chamado `universal-agent-skills`. Se for importar este pacote via Git local, deixe desmarcadas as opções de gerar README, `.gitignore` e licença, porque os dois primeiros já vêm no pacote e a licença depende da sua escolha.

## No computador
Abra o terminal na pasta `universal-agent-skills` e execute:

```bash
git init
git branch -M main
git add .
git status
git diff --cached --name-only
git commit -m "feat: add portable agent skills library v1"
git remote add origin https://github.com/SEU-USUARIO/universal-agent-skills.git
git push -u origin main
```

Substitua `SEU-USUARIO` pelo seu usuário real e confirme que os arquivos do commit não incluem contextos particulares. Não execute `git add -f private`.

## Depois
- Ative Issues e use labels `skill`, `bug`, `enhancement`, `documentation`.
- Versão inicial, quando aprovada: `git tag v1.0.0` e `git push origin v1.0.0`.
- O GitHub Actions valida catálogo, skills e scripts em pushes e PRs.
