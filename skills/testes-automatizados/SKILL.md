---
name: testes-automatizados
description: "Use para definir e revisar testes Java/Spring, APIs e automações; priorize comportamento, casos-limite, isolamento e evidências de execução reais."
---

# Estratégia de testes e qualidade

## Princípio
Testar contrato e comportamento observável, não apenas cobertura numérica.

## Estratégia
1. Mapear requisito → cenário → critério de aceite → teste.
2. Separar unidade, slice/controller, integração/banco e teste manual/aceite.
3. Para Java/Spring, considerar JUnit 5, Mockito, MockMvc e testes de repositório/integração conforme dependências reais.
4. Cobrir fluxo feliz, bordas, erros, autorização, entrada inválida, duplicatas e transições de estado.
5. Evitar mocks de todas as camadas quando o objetivo é verificar integração real.
6. Inspecionar migrações, limpeza de estado, dados reproduzíveis e idempotência quando pertinentes.
7. Rodar apenas comandos seguros no ambiente disponível e registrar contagem e falhas sem inventar resultados.

## Exemplos de cenários
- REST: `200`, `201`, `204`, `400`, `401`, `403`, `404`, `409` conforme o contrato.
- JPA: paginação, consultas, transações, relações e constraints.
- Integração GLPI/Zabbix: indisponibilidade, timeout, paginação, autenticação e resposta inesperada sem vazar token.

## Revisão de testes
Classificar lacunas por risco: quebra de regra de negócio > segurança/dados > integrações > ergonomia. Sugerir testes adicionais antes de aumentar arquitetura por hipótese.
