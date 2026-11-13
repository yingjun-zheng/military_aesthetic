#!/usr/bin/env python
"""把一批生成图拼成对照图，方便一次挑图。

用法:
    python contact_sheet.py <图片目录> -o out.png --cols 3
    python contact_sheet.py a.png b.png c.png -o out.png

依赖 Pillow；缺失时给出安装提示后退出，不影响其他流程。
"""
import argparse
import os
import sys

IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".webp", ".bmp")

BG = (18, 16, 14)
PAD = 14
LABEL_H = 26


def load_pillow():
    try:
        from PIL import Image, ImageDraw, ImageFont
        return Image, ImageDraw, ImageFont
    except ImportError:
        print("缺少 Pillow，无法拼图。安装: pip install Pillow", file=sys.stderr)
        sys.exit(2)


def collect(paths):
    files = []
    for item in paths:
        if os.path.isdir(item):
            for name in sorted(os.listdir(item)):
                if name.lower().endswith(IMAGE_EXTS):
                    files.append(os.path.join(item, name))
        elif os.path.isfile(item):
            files.append(item)
        else:
            print("跳过不存在的路径: %s" % item, file=sys.stderr)
    return files


def main():
    parser = argparse.ArgumentParser(description="批量生成图拼成对照图")
    parser.add_argument("paths", nargs="+", help="图片目录或图片文件")
    parser.add_argument("-o", "--output", required=True, help="输出拼图路径")
    parser.add_argument("--cols", type=int, default=3, help="列数，默认 3")
    parser.add_argument("--thumb", type=int, default=520, help="缩略图宽度，默认 520")
    parser.add_argument("--labels", action="store_true", help="显示文件名")
    args = parser.parse_args()

    Image, ImageDraw, ImageFont = load_pillow()
    files = collect(args.paths)
    if not files:
        print("没有找到图片", file=sys.stderr)
        sys.exit(1)

    thumbs = []
    for path in files:
        try:
            im = Image.open(path).convert("RGB")
        except Exception as exc:  # 跳过坏文件
            print("跳过无法读取的文件 %s (%s)" % (path, exc), file=sys.stderr)
            continue
        ratio = args.thumb / im.width
        thumbs.append((path, im.resize((args.thumb, max(1, int(im.height * ratio))), Image.LANCZOS)))

    if not thumbs:
        print("没有可用图片", file=sys.stderr)
        sys.exit(1)

    cols = max(1, min(args.cols, len(thumbs)))
    rows = (len(thumbs) + cols - 1) // cols
    cell_h = max(t.height for _, t in thumbs) + (LABEL_H if args.labels else 0)
    sheet_w = cols * (args.thumb + PAD) + PAD
    sheet_h = rows * (cell_h + PAD) + PAD

    sheet = Image.new("RGB", (sheet_w, sheet_h), BG)
    draw = ImageDraw.Draw(sheet)
    font = None
    if args.labels:
        try:
            font = ImageFont.truetype("arial.ttf", 15)
        except Exception:
            font = ImageFont.load_default()

    for index, (path, thumb) in enumerate(thumbs):
        col = index % cols
        row = index // cols
        x = PAD + col * (args.thumb + PAD)
        y = PAD + row * (cell_h + PAD)
        sheet.paste(thumb, (x, y))
        if args.labels:
            name = os.path.basename(path)
            draw.text((x + 2, y + thumb.height + 5), name[:46], fill=(215, 205, 190), font=font)

    out_dir = os.path.dirname(os.path.abspath(args.output))
    if out_dir and not os.path.isdir(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    sheet.save(args.output)
    print("已生成对照图: %s (%d 张, %dx%d)" % (args.output, len(thumbs), sheet_w, sheet_h))


if __name__ == "__main__":
    main()
