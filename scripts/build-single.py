#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 docs/index.html 打包成自包含单文件（封面图内嵌 base64）。

用法（在仓库根目录执行）：
    python3 scripts/build-single.py

输出：docs/index_single.html  —— 可直接双击打开，不依赖 assets 目录。
注意：这是生成物，不要直接编辑，也不要提交进仓库。
"""
import re, base64, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'docs', 'index.html')
OUT = os.path.join(ROOT, 'docs', 'index_single.html')

def main():
    if not os.path.exists(SRC):
        print('找不到源文件:', SRC); sys.exit(1)
    src = open(SRC, encoding='utf-8').read()

    def to_data_uri(m):
        full = os.path.join(ROOT, 'docs', m.group(1))
        if not os.path.exists(full):
            print('  [跳过] 图片不存在:', m.group(1)); return m.group(0)
        with open(full, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode()
        return 'cover:"data:image/jpeg;base64,%s"' % b64

    out, n = re.subn(r'cover:"(assets/covers/[^"]+\.jpg)"', to_data_uri, src)
    open(OUT, 'w', encoding='utf-8').write(out)
    print('已生成: %s' % OUT)
    print('  大小: %s 字节 | 内联封面: %d 张' % (os.path.getsize(OUT), n))

if __name__ == '__main__':
    main()
