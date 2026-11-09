---
name: depuracao-com-evidencias
description: "Use para diagnosticar bugs, falhas de build, integração, rede ou desempenho sem adivinhar causas e sem mudanças destrutivas antes de medir."
---

# Debug orientado a evidências

## Princípio
Reproduzir, medir, isolar e validar uma hipótese por vez. Não atribuir causa a partir de um sintoma isolado.

## Fluxo
1. Coletar sintoma, comportamento esperado, erro exato, versão, ambiente e alteração recente.
2. Reproduzir no menor cenário seguro possível; registrar comandos e saída.
3. Listar até três hipóteses ordenadas por evidência e custo de teste.
4. Testar primeiro hipótese de baixo risco, com passo reversível e resultado esperado.
5. Corrigir apenas após confirmar causa provável; considerar regressões.
6. Executar teste que falhava e teste próximo; registrar o que foi validado.

## Exemplos relevantes
- Java/Spring: stack trace, `application.properties`, perfis, transações, SQL, API, autenticação, pool de conexões.
- Frontend: polling, cache, estado, CORS, chamadas duplicadas, logs de rede.
- Integrações: status HTTP, contrato, token sem exibição, limites e formatos de payload.
- Linux: versão do kernel, permissões, logs de serviço, processos, módulos e recursos.
- Windows: comandos PowerShell apropriados; não usar instruções Bash como se fossem equivalentes.

## Segurança operacional
Não alterar BIOS, banco, branch compartilhada, dados de produção ou sistema crítico sem consentimento explícito e alternativa de reversão. Proibido mascarar falhas com saída inventada.

## Modelo de resposta
**Sintoma** → **evidência** → **hipótese** → **teste de confirmação** → **resultado** → **correção mínima** → **reteste**.
