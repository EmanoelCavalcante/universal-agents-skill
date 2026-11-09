---
name: documentacao-git-e-decisoes
description: "Use ao documentar repositórios, produzir README/ADR, organizar branches, commits, changelog e registrar decisões técnicas verificadas."
---

# Documentação, Git e decisões técnicas

## Objetivo
Criar documentação curta, versionada, fiel ao estado real do projeto e útil a quem vai manter o código.

## Processo
1. Inspecionar a estrutura real do projeto e os arquivos de configuração; não inventar funcionalidades, dependências ou cobertura.
2. Redigir README com objetivo, requisitos, instalação, execução, testes, estrutura funcional e limitações verificadas.
3. Documentar decisões arquiteturais importantes com contexto, alternativas, escolha, consequências e data quando conhecida.
4. Para mudanças, gerar resumo claro dos arquivos afetados, motivo, comportamento e validação.
5. Usar Git conservadoramente: consultar status/diff antes de editar, não reverter mudanças alheias, não fazer force push nem commit sem pedido.
6. Em equipe, evitar expor segredos, `.env`, dados pessoais e detalhes internos.

## Preferências
Projetos acadêmicos devem explicar pesquisa e protótipo separadamente. Evitar complexidade documental desproporcional; diagramas Mermaid apenas quando esclarecem um fluxo. Não reescrever README com marketing ou claims falsos.

## Saída típica
Resumo da alteração; documentação atualizada; comandos testados; decisão tomada; limitações e próximos passos.
