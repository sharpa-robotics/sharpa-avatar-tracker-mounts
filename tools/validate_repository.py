"""Check the review package offline; does not certify hardware or CAD geometry."""

import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.transforms import ROOT, load_transform, validate_matrix


def main():
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)

    assets = json.loads((ROOT / 'catalog/assets.json').read_text(encoding='utf-8'))['assets']
    products = json.loads((ROOT / 'catalog/products.json').read_text(encoding='utf-8'))['products']
    paths = [a['path'] for a in assets]
    require(len(paths) == len(set(paths)), 'Duplicate catalog asset path')
    for a in assets:
        require(a['format'] == 'STEP' and Path(a['path']).suffix.lower() in ('.step', '.stp'),
                'Model format must be STEP: ' + a['path'])
        path = (ROOT / a['path']).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            errors.append('Missing or unsafe asset: ' + a['path'])
            continue
        payload = path.read_bytes()
        require(len(payload) == a['bytes'], 'Byte count mismatch: ' + a['path'])
        require(hashlib.sha256(payload).hexdigest() == a['sha256'], 'SHA-256 mismatch: ' + a['path'])
        if a['format'] == 'STEP':
            require(payload.startswith(b'ISO-10303-21;'), 'STEP header missing: ' + a['path'])
            require(payload.rstrip().endswith(b'END-ISO-10303-21;'), 'STEP footer missing: ' + a['path'])
            require(bool(re.search(rb'SI_UNIT\s*\(\s*\.MILLI\.\s*,\s*\.METRE\.\s*\)', payload)),
                    'STEP millimetre unit missing: ' + a['path'])

    actual_cad = {p.relative_to(ROOT).as_posix() for p in (ROOT / 'products').rglob('*')
                  if p.is_file() and 'cad' in p.relative_to(ROOT / 'products').parts}
    require(actual_cad == set(paths), 'CAD files and catalog are not synchronized')
    for p in products:
        try:
            data = load_transform(p['id'], allow_unvalidated=True)
            validate_matrix(data['source_matrix'])
            require(data['source_translation_unit_interpretation'] == 'mm', 'Unexpected source unit')
            for i in range(4):
                for j in range(4):
                    expected = data['source_matrix'][i][j]
                    if i < 3 and j == 3:
                        expected /= 1000
                    require(abs(data['matrix'][i][j] - expected) < 1e-12,
                            f'Matrix unit conversion mismatch: {p["id"]}[{i},{j}]')
            product_path = ROOT / f'products/{p["id"]}/product.json'
            require(json.loads(product_path.read_text(encoding='utf-8')) == p,
                    'Product metadata differs from catalog: ' + p['id'])
            for path in p['assets']:
                require(path in paths, 'Unknown product asset: ' + path)
        except (ValueError, KeyError, OSError, TypeError) as exc:
            errors.append(p['id'] + ': ' + str(exc))

    link_count = 0
    text_count = 0
    for path in ROOT.rglob('*'):
        if not path.is_file() or '.git' in path.parts or path.suffix not in ('.md', '.json', '.py', '.yml', '.txt'):
            continue
        text = path.read_text(encoding='utf-8')
        text_count += 1
        require(not re.search(r'https?://[^\s"<>)]*(?:feishu\.cn|larksuite\.com)', text),
                'Internal source URL in public draft: ' + str(path.relative_to(ROOT)))
        if path.suffix != '.md':
            continue
        for target in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)\)', text):
            parsed = urlsplit(target)
            if parsed.scheme or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            link_count += 1
            require(resolved.is_relative_to(ROOT) and resolved.exists(),
                    f'Broken local file link: {path.relative_to(ROOT)} -> {target}')
    if errors:
        for error in errors:
            print('ERROR: ' + error)
        return 1
    print(f'PASS: {len(assets)} CAD files, {len(products)} transforms, {link_count} local file links, {text_count} text files.')
    print('STEP envelopes and mm units checked. CAD geometry, printability and hardware validation remain pending.')
    print('License is pending review; this is a public preview, not a release certification.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
