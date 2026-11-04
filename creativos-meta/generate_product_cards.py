import os
import subprocess
from PIL import Image, ImageDraw, ImageFilter

BASE_DIR = "/home/fran/Programming/landing-excel-finanzas"
OUT_CARROUSEL = f"{BASE_DIR}/creativos-meta/carrusel-producto"
OUT_CLEAN = f"{BASE_DIR}/creativos-meta/mockups-cuadrados"

os.makedirs(OUT_CARROUSEL, exist_ok=True)
os.makedirs(OUT_CLEAN, exist_ok=True)

# 1. GENERATE AD-READY PRODUCT CARDS VIA RSVG-CONVERT
product_cards = [
    {
        "num": 1,
        "title": "Tu sistema financiero completo",
        "tag": "MULTIDISPOSITIVO",
        "img": f"{BASE_DIR}/images/finanzas360-mockup.jpg",
        "pill": "Google Sheets &amp; Excel · Celular, Tablet y PC",
        "aspect": "landscape"
    },
    {
        "num": 2,
        "title": "Todo en una sola planilla",
        "tag": "ECOSISTEMA 360",
        "img": f"{BASE_DIR}/images/gallery-overview.jpg",
        "pill": "5 hubs integrados · Cero apps duplicadas",
        "aspect": "square"
    },
    {
        "num": 3,
        "title": "Panel diario en 30 segundos",
        "tag": "FOCO &amp; CLARIDAD",
        "img": f"{BASE_DIR}/images/gallery-dashboard.jpg",
        "pill": "Métricas en tiempo real · Alertas automáticas",
        "aspect": "portrait"
    },
    {
        "num": 4,
        "title": "Cuotas, tarjetas y ahorro",
        "tag": "CONTROL TOTAL",
        "img": f"{BASE_DIR}/images/gallery-finanzas.jpg",
        "pill": "Regla de los 4 bolsillos · Sin sorpresas",
        "aspect": "landscape"
    },
    {
        "num": 5,
        "title": "Tus metas a 90 días, claras",
        "tag": "ACCIÓN &amp; LOGROS",
        "img": f"{BASE_DIR}/images/gallery-metas.jpg",
        "pill": "Metodología trimestral · Progreso automático",
        "aspect": "portrait"
    },
    {
        "num": 6,
        "title": "Hábitos, sueño y bienestar",
        "tag": "RUTINAS &amp; ENERGÍA",
        "img": f"{BASE_DIR}/images/gallery-bienestar.jpg",
        "pill": "Diseño anti-culpa · Consistencia diaria",
        "aspect": "landscape"
    }
]

for card in product_cards:
    n = card["num"]
    title = card["title"]
    tag = card["tag"]
    img_path = card["img"]
    pill = card["pill"]
    aspect = card["aspect"]
    
    # Calculate box coordinates based on aspect ratio
    if aspect == "portrait":
        # narrower, taller
        box_w, box_h = 580, 680
        box_x = (1080 - box_w) // 2
        box_y = 245
    elif aspect == "square":
        box_w, box_h = 680, 680
        box_x = (1080 - box_w) // 2
        box_y = 245
    else: # landscape
        box_w, box_h = 860, 640
        box_x = (1080 - box_w) // 2
        box_y = 265

    clip_id = f"clip_{n}"
    svg_code = f"""<svg width="1080" height="1080" viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="125%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="16" stdDeviation="24" flood-color="#000000" flood-opacity="0.10" />
    </filter>
    <clipPath id="{clip_id}">
      <rect x="{box_x}" y="{box_y}" width="{box_w}" height="{box_h}" rx="24" ry="24" />
    </clipPath>
  </defs>

  <!-- Background -->
  <rect width="1080" height="1080" fill="#F5F3EC" />

  <!-- Organic background curves -->
  <path d="M-50,200 Q200,50 400,250 T800,100 T1150,300" fill="none" stroke="#EAE6DC" stroke-width="2" opacity="0.6"/>
  <path d="M-100,850 Q300,700 600,950 T1150,800" fill="none" stroke="#EAE6DC" stroke-width="2" opacity="0.6"/>
  <circle cx="950" cy="180" r="140" fill="#EFECE3" opacity="0.7"/>
  <circle cx="120" cy="920" r="160" fill="#EFECE3" opacity="0.7"/>

  <!-- Top Title -->
  <text x="540" y="130" font-family="'DejaVu Serif', Georgia, serif" font-size="44" font-weight="bold" fill="#1E2229" text-anchor="middle" letter-spacing="-0.5">
    {title}
  </text>

  <!-- Subtitle Tag Pill -->
  <g transform="translate(540, 175)">
    <rect x="-110" y="0" width="220" height="34" rx="17" fill="#E3EAE4"/>
    <text x="0" y="22" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#2C4F3B" text-anchor="middle" letter-spacing="1.2">
      {tag}
    </text>
  </g>

  <!-- Card Background with Shadow -->
  <rect x="{box_x}" y="{box_y}" width="{box_w}" height="{box_h}" rx="24" ry="24" fill="#FFFFFF" filter="url(#shadow)" stroke="#E6E2D8" stroke-width="2" />

  <!-- Image with Clip -->
  <g clip-path="url(#{clip_id})">
    <image href="{img_path}" x="{box_x}" y="{box_y}" width="{box_w}" height="{box_h}" preserveAspectRatio="xMidYMid slice" />
  </g>

  <!-- Card Border On Top of Image -->
  <rect x="{box_x}" y="{box_y}" width="{box_w}" height="{box_h}" rx="24" ry="24" fill="none" stroke="#E6E2D8" stroke-width="2" />

  <!-- Benefit Highlight Pill Bottom -->
  <g transform="translate(540, 945)">
    <rect x="-240" y="-18" width="480" height="36" rx="18" fill="#FFFFFF" stroke="#E2E8F0" filter="url(#shadow)"/>
    <circle cx="-215" cy="0" r="8" fill="#10B981"/>
    <text x="-215" y="4" font-family="'DejaVu Sans', sans-serif" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle">✓</text>
    <text x="-195" y="5" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="600" fill="#1E293B">
      {pill}
    </text>
  </g>

  <!-- Slide Counter -->
  <g transform="translate(540, 1018)">
    <rect x="-55" y="-16" width="110" height="28" rx="14" fill="#EAE5DC"/>
    <text x="0" y="2" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#78716C" text-anchor="middle">
      {n} / 6
    </text>
  </g>
</svg>"""

    svg_file = f"{OUT_CARROUSEL}/prod_card_{n}.svg"
    png_file = f"{OUT_CARROUSEL}/prod_card_{n}.png"

    with open(svg_file, "w", encoding="utf-8") as f:
        f.write(svg_code)

    cmd = ["rsvg-convert", "-w", "1080", "-h", "1080", "-f", "png", "-o", png_file, svg_file]
    subprocess.run(cmd, check=True)
    print(f"Generated {png_file}")

# 2. GENERATE PURE CLEAN SQUARE MOCKUPS (1080x1080)
clean_items = [
    ("mockup_general_square.png", f"{BASE_DIR}/images/finanzas360-mockup.jpg"),
    ("gallery_overview_square.png", f"{BASE_DIR}/images/gallery-overview.jpg"),
    ("gallery_dashboard_square.png", f"{BASE_DIR}/images/gallery-dashboard.jpg"),
    ("gallery_finanzas_square.png", f"{BASE_DIR}/images/gallery-finanzas.jpg"),
    ("gallery_metas_square.png", f"{BASE_DIR}/images/gallery-metas.jpg"),
    ("gallery_bienestar_square.png", f"{BASE_DIR}/images/gallery-bienestar.jpg"),
]

for out_name, src_path in clean_items:
    out_file = f"{OUT_CLEAN}/{out_name}"
    src = Image.open(src_path).convert("RGBA")
    sw, sh = src.size
    
    max_side = 960
    scale = min(max_side / sw, max_side / sh)
    nw, nh = int(sw * scale), int(sh * scale)
    src_resized = src.resize((nw, nh), Image.Resampling.LANCZOS)
    
    # Mask with rounded corners
    mask = Image.new("L", (nw, nh), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.rounded_rectangle([(0, 0), (nw, nh)], radius=28, fill=255)
    
    # Soft drop shadow
    pad = 40
    shadow = Image.new("RGBA", (nw + pad*2, nh + pad*2), (0, 0, 0, 0))
    draw_shadow = ImageDraw.Draw(shadow)
    draw_shadow.rounded_rectangle([(pad, pad + 12), (nw + pad, nh + pad + 12)], radius=28, fill=(0, 0, 0, 50))
    shadow = shadow.filter(ImageFilter.GaussianBlur(22))
    
    # 1080x1080 canvas
    canvas = Image.new("RGB", (1080, 1080), (245, 243, 236))
    
    cx = (1080 - nw) // 2
    cy = (1080 - nh) // 2
    
    canvas.paste(shadow, (cx - pad, cy - pad), shadow)
    canvas.paste(src_resized, (cx, cy), mask)
    
    # Border
    border = Image.new("RGBA", (nw, nh), (0, 0, 0, 0))
    draw_border = ImageDraw.Draw(border)
    draw_border.rounded_rectangle([(0, 0), (nw-1, nh-1)], radius=28, outline=(230, 226, 216, 255), width=2)
    canvas.paste(border, (cx, cy), border)
    
    canvas.save(out_file, quality=96)
    print(f"Generated clean square: {out_file}")

print("All product cards and clean square mockups created!")
