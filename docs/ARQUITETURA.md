# Arquitetura da biblioteca

## Uma única fonte da verdade
Cada skill existe apenas em `skills/<slug>/SKILL.md`; não mantenha cópias manuais divergentes em `.claude`, `.agents`, `.gemini`, `.cursor` ou `.github`.

## Componentes
- **Skills:** instruções acionadas mediante relevância, aderentes à especificação Agent Skills.
- **Adapters:** instruções gerais persistentes, com sintaxe de cada agente. Não substituem skills.
- **Templates:** estruturas preenchíveis e não sensíveis.
- **Private:** perfis e contextos locais, nunca enviados ao controle de versão.
- **Scripts:** instalação, validação e exportação, sem dependências externas.

## Padrões de qualidade
Cada skill deve ter `name` igual ao diretório, `description` informando quando usar, seções de procedimento, limites e resultado esperado. A seleção é contextual: evitar carregar todas as skills ao mesmo tempo.

## Compatibilidade
O padrão dos arquivos é compartilhado, mas recursos como ferramentas autorizadas, permissões, comandos e descoberta são específicos de cada agente. Mantenha o frontmatter canônico com os campos obrigatórios (`name`, `description`) e trate campos específicos em adapters futuros.

## Versionamento
Use tags `vMAJOR.MINOR.PATCH`. Correções sem mudança de intenção: PATCH; ampliação compatível de procedimentos: MINOR; alteração de contrato ou comportamento esperado: MAJOR.
