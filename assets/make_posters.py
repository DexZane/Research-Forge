#!/usr/bin/env python3
"""Compose exact-copy Research Forge promo assets over generated visual backgrounds."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source"

TITLE_FONT = "/System/Library/Fonts/Supplemental/Savoye LET.ttc"
DISPLAY_FONT = "/System/Library/Fonts/Supplemental/Bodoni 72 Smallcaps Book.ttf"
# Hiragino Sans GB has broad Simplified Chinese coverage; the title still carries
# the artistic display treatment while Chinese copy stays legible and complete.
CN_DISPLAY_FONT = "/System/Library/Fonts/Hiragino Sans GB.ttc"
CN_BODY_FONT = "/System/Library/Fonts/Hiragino Sans GB.ttc"

NAVY = (5, 18, 38, 255)
INK = (228, 239, 248, 255)
MUTED = (175, 195, 211, 255)
ORANGE = (255, 178, 53, 255)
GOLD = (255, 212, 112, 255)


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


def fit_font(text: str, path: str, max_width: int, start: int, minimum: int = 18) -> ImageFont.FreeTypeFont:
    size = start
    while size > minimum:
        candidate = font(path, size)
        if candidate.getbbox(text)[2] <= max_width:
            return candidate
        size -= 2
    return font(path, minimum)


def add_left_gradient(image: Image.Image, width: int, opacity: int = 210) -> Image.Image:
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    pixels = overlay.load()
    for x in range(min(width, image.width)):
        alpha = int(opacity * (1 - x / max(width, 1)) ** 0.72)
        for y in range(image.height):
            pixels[x, y] = (2, 12, 29, alpha)
    return Image.alpha_composite(image.convert("RGBA"), overlay)


def draw_glow(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt: ImageFont.FreeTypeFont, fill: tuple[int, int, int, int], anchor: str = "lt") -> None:
    x, y = xy
    draw.text((x + 4, y + 7), text, font=fnt, fill=(255, 135, 20, 115), anchor=anchor, stroke_width=5, stroke_fill=(255, 135, 20, 70))
    draw.text((x, y), text, font=fnt, fill=fill, anchor=anchor, stroke_width=1, stroke_fill=(255, 232, 174, 180))


def rounded_label(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt: ImageFont.FreeTypeFont, fill=(255, 178, 53, 255)) -> None:
    x, y = xy
    box = draw.textbbox((x, y), text, font=fnt, anchor="lt")
    pad_x, pad_y = 16, 8
    draw.rounded_rectangle((box[0] - pad_x, box[1] - pad_y, box[2] + pad_x, box[3] + pad_y), radius=9, fill=(5, 18, 38, 255), outline=(255, 178, 53, 255), width=2)
    draw.text((x, y), text, font=fnt, fill=fill, anchor="lt")


def compose_banner(background: Path, output: Path, chinese: bool) -> None:
    image = add_left_gradient(Image.open(background).convert("RGBA"), width=1120)
    draw = ImageDraw.Draw(image)
    x = 90
    if chinese:
        tag = font(CN_BODY_FONT, 24)
        title = fit_font("Research Forge", TITLE_FONT, 820, 132, 92)
        subtitle_text = "面向 AI 与深度学习的对抗式科研选题 Skill"
        subtitle_font = fit_font(subtitle_text, CN_BODY_FONT, 890, 43, 28)
        rule = "搜索以拒绝  ·  假设先于架构  ·  证伪先于优化"
        footer = "S00–S18  ·  四个人工 Gate  ·  Zotero/BibTeX"
        rounded_label(draw, (x, 70), "AI METHOD RESEARCH  /  OPEN SOURCE", tag)
        draw_glow(draw, (x, 146), "Research Forge", title, GOLD)
        draw.text((x, 300), subtitle_text, font=subtitle_font, fill=INK, anchor="lt")
        draw.line((x, 390, x + 650, 390), fill=ORANGE, width=3)
        draw.text((x, 425), rule, font=font(CN_BODY_FONT, 31), fill=MUTED, anchor="lt")
        draw.text((x, 654), footer, font=font(CN_BODY_FONT, 25), fill=(255, 220, 145, 245), anchor="lt")
    else:
        tag = font(DISPLAY_FONT, 24)
        title = fit_font("Research Forge", TITLE_FONT, 840, 138, 96)
        subtitle_text = "Adversarial research direction for AI & deep learning"
        subtitle_font = fit_font(subtitle_text, DISPLAY_FONT, 900, 43, 28)
        rule = "Search to reject  ·  Hypothesis before architecture  ·  Falsification before optimization"
        footer = "S00–S18  ·  HUMAN GATES  ·  EVIDENCE > DECISION"
        rounded_label(draw, (x, 70), "OPEN-SOURCE RESEARCH SKILL", tag)
        draw_glow(draw, (x, 146), "Research Forge", title, GOLD)
        draw.text((x, 300), subtitle_text, font=subtitle_font, fill=INK, anchor="lt")
        draw.line((x, 390, x + 650, 390), fill=ORANGE, width=3)
        draw.text((x, 425), rule, font=font(DISPLAY_FONT, 28), fill=MUTED, anchor="lt")
        draw.text((x, 654), footer, font=font(DISPLAY_FONT, 25), fill=(255, 220, 145, 245), anchor="lt")
    image.convert("RGB").save(output, quality=96, optimize=True)


def compose_poster(background: Path, output: Path) -> None:
    image = Image.open(background).convert("RGBA")
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    over_draw = ImageDraw.Draw(overlay)
    over_draw.rectangle((0, 0, image.width, 650), fill=(2, 12, 29, 110))
    image = Image.alpha_composite(image, overlay)
    draw = ImageDraw.Draw(image)
    x = 92
    rounded_label(draw, (x, 76), "AI METHOD RESEARCH  /  OPEN SOURCE", font(CN_BODY_FONT, 24))
    draw_glow(draw, (x, 150), "Research Forge", fit_font("Research Forge", TITLE_FONT, 920, 140, 98), GOLD)

    quote_font = font(CN_DISPLAY_FONT, 55)
    draw.text((x, 318), "别问想法听起来是否新颖，", font=quote_font, fill=INK, anchor="lt")
    draw.text((x, 392), "先尝试证明它并不新颖。", font=quote_font, fill=GOLD, anchor="lt")
    draw.line((x, 500, x + 550, 500), fill=ORANGE, width=4)

    body = font(CN_BODY_FONT, 31)
    cards = [
        "文献攻击：搜索以拒绝，而不是确认",
        "机制假设：先于架构，必须可预测",
        "最低成本证伪：先做能杀死主张的测试",
        "四个人工 Gate：范围、候选、假设、启动",
        "Zotero/BibTeX：核验书目，导入后精读",
    ]
    top = 570
    for index, text in enumerate(cards):
        y = top + index * 102
        draw.rounded_rectangle((x, y, image.width - x, y + 72), radius=14, fill=(5, 18, 38, 195), outline=(255, 178, 53, 130), width=2)
        draw.ellipse((x + 20, y + 24, x + 36, y + 40), fill=ORANGE)
        draw.text((x + 56, y + 18), text, font=body, fill=INK, anchor="lt")

    draw.text((x, 1255), "从模糊方向到可验证项目决策", font=font(CN_DISPLAY_FONT, 34), fill=GOLD, anchor="lt")
    draw.text((x, 1320), "github.com/DexZane/Research-Forge", font=font(DISPLAY_FONT, 27), fill=MUTED, anchor="lt")
    image.convert("RGB").save(output, quality=96, optimize=True)


def main() -> None:
    compose_banner(SOURCE / "forge-landscape-background.png", ROOT / "research-forge-banner-en.png", chinese=False)
    compose_banner(SOURCE / "forge-landscape-background.png", ROOT / "research-forge-banner-zh.png", chinese=True)
    compose_poster(SOURCE / "forge-portrait-background.png", ROOT / "research-forge-poster-zh.png")


if __name__ == "__main__":
    main()
