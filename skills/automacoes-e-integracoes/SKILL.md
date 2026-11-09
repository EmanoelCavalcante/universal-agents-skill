---
name: automacoes-e-integracoes
description: "Use em integração de sistemas corporativos, GLPI, Zabbix e processos com planilhas ou arquivos; prefira automações verificáveis sem interface paralela."
---

# Automações e integrações de TI

## Contexto
Experiência de trabalho com GLPI, Zabbix, inventário, documentação, planilhas e gestão à vista. Nem toda automação corporativa usa a mesma versão/instalação: verificar ambiente atual e documentação oficial.

## Preferências recorrentes
- Centralizar fluxos no sistema existente quando viável, **sem criar interface paralela** sem necessidade.
- Rapidez de entrega com validação objetiva.
- PHP pode ser adequado em plugins GLPI; Java ou outra linguagem só quando o contexto justificar.
- Tarefas com dados, mapas, screenshots e relatórios devem gerar evidência rastreável, não números fictícios.

## Procedimento
1. Mapear sistema de origem, destino, autenticação, autorização, dados disponíveis e consumidor final.
2. Conferir contratos reais de API, versão, paginação, códigos de erro, limites e rate limits.
3. Preferir integração de menor acoplamento e rastreabilidade (adapter quando fizer sentido).
4. Projetar para idempotência, duplicatas, falhas parciais e logs sem segredos.
5. Testar primeiro em ambiente seguro; prever retry limitado e fallback.
6. Reconciliar resultado com origem antes de atualizar chamados, relatórios, planilhas ou dashboards.

## Cuidados adicionais
Nunca registrar tokens em repositório, prompt, prints ou documentação pública. Não enviar dados internos a serviços externos nem modificar produção sem autorização. Se uma API não estiver disponível, informar a limitação em vez de simular integração.
