---
name: auditoria-de-entrega
description: "Use antes de aprovar release, automação, relatório ou tarefa concluída; compare critérios de aceite com testes, evidências, riscos e pendências reais."
---

# Auditoria de entrega e aceite

## Pergunta central
**O que prova que a entrega funciona no cenário solicitado?**

## Checklist operacional
1. Reconstituir escopo aprovado e critérios de aceite.
2. Conferir alterações concretas contra o escopo, incluindo arquivos não relacionados e impactos.
3. Confirmar build, testes, casos de erro, permissões e migrações aplicáveis.
4. Validar outputs (API, arquivo, screenshot, relatório) com origem, data e rastreabilidade.
5. Checar rollback e backup quando há alteração de dados/produção.
6. Inspecionar exposição de segredos, credenciais, endpoints internos ou dados pessoais.
7. Classificar resultado em **Aprovado**, **Aprovado com ressalvas** ou **Bloqueado**, com justificativa.

## Cuidados
Não deduzir que `0 falhas` histórico significa testes atuais aprovados. Não declarar integrado, enviado ou implantado quando apenas código foi gerado. Não automatizar ação externa de risco sem autorização.

## Relatório curto
**Escopo verificado**; **Evidências**; **Testes realizados / não realizados**; **Riscos e pendências**; **Decisão**; **Próxima ação**.
