---
name: backend-java-spring
description: "Use para orientar ou implementar backend Java e Spring Boot com APIs REST, JPA, validação, segurança, migrações, DTOs e padrões adequados ao projeto."
---

# Backend Java / Spring Boot pragmático

## Escopo
Java moderno, Spring Boot, REST, DTOs, Bean Validation, JPA/Hibernate, Spring Security/JWT quando necessário, SQL relacional, Flyway, Maven, documentação OpenAPI.

## Antes de propor solução
1. Confirmar Java, versão do Spring e dependências **reais do repositório**; não assumir versões históricas.
2. Inspecionar convenções: pacotes, service/controller/repository, mapeadores, transações, tratamento de erros, testes e migrações.
3. Distinguir arquitetura existente (camadas MVC, hexagonal, modular) de arquitetura idealizada. **Não refatorar para hexagonal ou Clean Architecture por moda.**
4. Identificar requisito, contrato API, invariantes do domínio e riscos de regressão.

## Critérios técnicos
- Controllers finos; regras de negócio na camada apropriada.
- DTOs de entrada/saída e validação em limites; não vazar entidades indevidamente.
- Consistência de erros HTTP, paginação, filtros e ordenação estável.
- Transações explícitas quando necessárias; tratar N+1, limites de consulta e paginação.
- Não introduzir JWT, cache, eventos ou microserviços sem requisito.
- SQL, índices, constraints e migrações versionadas quando pertinentes.
- Logs úteis sem segredos; não presumir sucesso sem execução de testes.

## Trabalhar no modo correto
No projeto pessoal/estudantil, priorizar mentoria e revisão incremental. Na tarefa empresarial expressamente autorizada, executar a mudança mínima com teste e resumo. Preferência do projeto prevalece sobre preferência geral.

## Entrega esperada
Decisão técnica e motivo; arquivos afetados; contrato/fluxo; casos de teste; limites e riscos. Código somente quando solicitado ou autorizado pelo modo de execução.
