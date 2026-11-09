---
name: implementacao-agil-controlada
description: "Use quando o usuário autorizar entrega rápida de código ou automação corporativa; implemente com escopo mínimo, testes e segurança, sem reescrever tudo."
---

# Execução rápida, controlada e verificável

## Quando usar
O usuário pediu explicitamente que a IA implemente, automatize, corrija ou entregue algo pronto, sobretudo em rotinas corporativas ou freelas de prazo curto.

## Fluxo de execução
1. Confirmar objetivo operacional, entradas, saídas, sistemas envolvidos e critérios de aceite.
2. Inspecionar arquivos e componentes atuais antes de editar; respeitar alterações locais, branch e convenções.
3. Priorizar o menor caminho que resolve o problema, sem interface nova, dependências grandes ou refatorações paralelas.
4. Planejar mudanças com risco e rollback; pedir aprovação apenas em ações destrutivas, irreversíveis, externas ou de alto impacto.
5. Implementar em passos pequenos e validar por teste, comando ou evidência observável.
6. Entregar resumo claro de arquivos, comportamento, testes realizados e pendências.

## Restrições fortes
- Nunca publicar, enviar mensagens externas, apagar dados, trocar credenciais, forçar push, executar operações de produção ou criar contas sem autorização.
- Não sobrescrever mudanças não relacionadas do usuário.
- Não declarar execução ou sucesso de testes que não rodaram.
- Em ambientes corporativos, não copiar dados sensíveis para locais públicos nem expor tokens.

## Modo híbrido
Se o usuário pedir agilidade com aprendizado (como em PHP/GLPI), incluir apenas a explicação mínima do trecho crítico e apontar como testá-lo. Evitar aula extensa.

## Saída
**Entregue:** ... **Arquivos:** ... **Teste/evidência:** ... **Limites:** ... **Rollback (se aplicável):** ...
