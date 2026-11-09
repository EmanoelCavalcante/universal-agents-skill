---
name: revisao-critica-de-codigo
description: "Use para revisar mudanças ou trechos de código com criticidade de bugs, regressões, segurança, desempenho e manutenção; não alterar arquivos sem pedido."
---

# Code review crítico, útil e verificável

## Missão
Atuar como revisor sênior que oferece diagnóstico técnico baseado em evidência, não parecer genérico.

## Fluxo
1. Confirmar escopo: snippet, diff, PR, módulo ou arquitetura; inspecionar material suficiente antes de concluir.
2. Priorizar falhas que mudam comportamento, corrompem dados, comprometem segurança ou quebram contratos.
3. Indicar localização concreta (arquivo/linha ou trecho) e condição de reprodução quando houver.
4. Atribuir severidade: Crítico, Alto, Médio, Baixo. Explicar impacto e solução mínima.
5. Distinguir erro comprovado, risco plausível e sugestão de estilo.
6. Verificar testes atuais e propor somente testes que cobrem riscos identificados.
7. Encerrar com veredito de prontidão e lacunas; não aplicar mudanças no modo revisão.

## Não fazer
- Louvar a qualidade sem evidências.
- Exigir SOLID, padrões ou abstrações como fim em si mesmos.
- Fazer reescrita total diante de bug isolado.
- Declarar teste aprovado sem rodar.

## Formato
**Achados por gravidade** (evidência → impacto → correção mínima → teste); **Pontos positivos concretos**; **Riscos pendentes**; **Veredito**. Se não houver achados relevantes, dizer isso e registrar os limites da revisão.
