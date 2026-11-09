#!/usr/bin/env python3
"""Confere organização e cabeçalhos mínimos Agent Skills (stdlib)."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
CATALOG = ROOT / "CATALOGO.json"
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

def frontmatter(content: str):
    lines = content.splitlines()
    if not lines or lines[0] != "---":
        return None
    try:
        ending = lines.index("---", 1)
    except ValueError:
        return None
    result = {}
    for line in lines[1:ending]:
        match = re.match(r"^(name|description):\s*(.*)$", line)
        if match:
            raw = match.group(2).strip()
            if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in ('"', "'"):
                raw = raw[1:-1]
            result[match.group(1)] = raw
    return result

def main():
    errors = []
    try:
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"ERRO: catálogo inválido: {exc}")
        return 1
    category_list = catalog.get("categories", {})
    names = [name for entries in category_list.values() for name in entries]
    if len(names) != len(set(names)):
        errors.append("Nomes duplicados no catálogo")
    if catalog.get("total") != len(names):
        errors.append("Total não coincide com o catálogo")
    discovered = sorted(p.parent.name for p in SKILLS.glob("*/SKILL.md"))
    if sorted(names) != discovered:
        errors.append("Inconsistência entre skills/ e CATALOGO.json")
    for skill in sorted(SKILLS.iterdir()):
        if not skill.is_dir():
            continue
        path = skill / "SKILL.md"
        if not path.exists():
            errors.append(f"Falta SKILL.md: {skill.name}")
            continue
        content = path.read_text(encoding="utf-8")
        info = frontmatter(content)
        if not info:
            errors.append(f"Frontmatter ausente/fora do padrão: {skill.name}")
            continue
        name = info.get('name', '')
        desc = info.get('description', '')
        if name != skill.name or not NAME.fullmatch(name) or len(name)>64:
            errors.append(f"Nome inválido em {path}")
        if not 1 <= len(desc) <= 1024:
            errors.append(f"Descrição ausente/fora do limite: {path}")
        if not content.split('---', 2)[-1].strip():
            errors.append(f"Corpo vazio: {path}")
        if re.search(r"\bghp_[A-Za-z0-9]{30,}\b|\bsk-[A-Za-z0-9_-]{20,}\b|AKIA[0-9A-Z]{16}", content):
            errors.append(f"Possível token em {path} — inspecionar")
    if errors:
        for err in errors: print('ERRO:', err)
        return 1
    print(f"OK: {len(discovered)} skills, metadados e catálogo consistentes.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
