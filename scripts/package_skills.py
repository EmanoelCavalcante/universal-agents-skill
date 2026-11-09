#!/usr/bin/env python3
"""Cria ZIP individual, com diretório-raiz <skill-name>/SKILL.md, para upload manual."""
import argparse
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--skill', action='append', help='Nome de uma skill; padrão: todas')
parser.add_argument('--out', type=Path, default=ROOT / 'dist')
args = parser.parse_args()
src = ROOT / 'skills'
names = args.skill or sorted(p.name for p in src.iterdir() if (p/'SKILL.md').is_file())
args.out.mkdir(parents=True, exist_ok=True)
for name in names:
    directory = src / name
    if not (directory/'SKILL.md').is_file():
        parser.error(f'Skill desconhecida: {name}')
    path = args.out / f'{name}.zip'
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for file in directory.rglob('*'):
            if file.is_file(): z.write(file, file.relative_to(src))
    print(path)
