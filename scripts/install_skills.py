#!/usr/bin/env python3
"""Copia skills canônicas aos locais dos agentes (sem sobrescrever por padrão)."""
import argparse
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / 'skills'
PROJECT = {
    'claude': Path('.claude/skills'),
    'codex': Path('.agents/skills'),
    'gemini': Path('.gemini/skills'),
    'cursor': Path('.cursor/skills'),
    'copilot': Path('.github/skills'),
}
PERSONAL = {
    'claude': Path('.claude/skills'),
    'codex': Path('.agents/skills'),
    'gemini': Path('.gemini/skills'),
    'cursor': Path('.cursor/skills'),
    'copilot': Path('.copilot/skills'),
}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agent', required=True, choices=(*PROJECT.keys(), 'all'))
    parser.add_argument('--scope', required=True, choices=('project', 'user'))
    parser.add_argument('--target', type=Path, help='Raiz do projeto, obrigatório com --scope project')
    parser.add_argument('--skill', action='append', help='Nome de uma skill; repita a opção para várias. Padrão: todas.')
    parser.add_argument('--force', action='store_true', help='Substitui diretório da skill já existente (CUIDADO).')
    args = parser.parse_args()
    if args.scope == 'project' and args.target is None:
        parser.error('--target é obrigatório para --scope project')
    if args.scope == 'user' and args.target is not None:
        parser.error('--target só pode ser usado em --scope project')
    base = args.target.resolve() if args.scope == 'project' else Path.home()
    if not base.is_dir():
        parser.error(f'Diretório não encontrado: {base}')
    names = args.skill or sorted(p.name for p in SOURCES.iterdir() if (p/'SKILL.md').is_file())
    invalid = [name for name in names if not (SOURCES/name/'SKILL.md').is_file() or name in ('.', '..')]
    if invalid:
        parser.error(f'Skill(s) desconhecidas: {invalid}')
    destinations = PROJECT if args.scope == 'project' else PERSONAL
    agents = list(PROJECT.keys()) if args.agent == 'all' else [args.agent]
    num = skipped = 0
    for agent in agents:
        path = base / destinations[agent]
        for name in names:
            dst = path / name
            if dst.exists() and not args.force:
                print(f'IGNORADO (já existe): {dst}')
                skipped += 1
                continue
            # Opção --force só remove skill existente com SKILL.md para evitar apagar conteúdo inesperado.
            if dst.exists():
                if not (dst/'SKILL.md').is_file() or dst.is_symlink():
                    parser.error(f'Destino não parece skill normal, não removido: {dst}')
                shutil.rmtree(dst)
            path.mkdir(parents=True, exist_ok=True)
            shutil.copytree(SOURCES/name, dst)
            print(f'INSTALADO [{agent}]: {dst}')
            num += 1
    print(f'Concluído: {num} cópia(s), {skipped} ignorada(s).')
    return 0

if __name__ == '__main__':
    sys.exit(main())
