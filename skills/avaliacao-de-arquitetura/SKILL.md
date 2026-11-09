---
name: avaliacao-de-arquitetura
description: "Use para comparar MVC em camadas, hexagonal e outras abordagens, julgar trade-offs e detectar acoplamento, abstrações prematuras e riscos reais."
---

# Avaliação arquitetural pragmática

## Objetivo
Decidir a arquitetura adequada ao domínio, maturidade e restrições; não transformar preferência estética em regra universal.

## Procedimento
1. Levantar contexto: tamanho, domínio, equipe, prazo, perfil de mudança, requisitos não funcionais.
2. Identificar a arquitetura implementada a partir das dependências e do código, não do nome das pastas.
3. Avaliar coesão, acoplamento, direção de dependências, limites transacionais, testabilidade, complexidade operacional e custo de manutenção.
4. Comparar opções (camadas/MVC, ports-and-adapters, modular monolith etc.) com trade-offs concretos.
5. Preservar decisões do projeto: PetCare usa abordagem hexagonal; Manutenção Preventiva retornou a camadas MVC. Não aplicar uma decisão ao outro.
6. Recomendar mudança incremental apenas quando o benefício superar custo, risco e regressão.

## Rubrica orientativa (0–5 por critério)
Correção de responsabilidades; isolamento do domínio; testabilidade; clareza das interfaces; simplicidade; adequação ao requisito.

## Saída
Arquitetura constatada; problemas com evidências; alternativas e impactos; recomendação de menor risco; experimento ou teste para validar o trade-off.
