# 📱 Creativos Meta Ads (Carrusel 1:1 · 1080x1080 px)

Colección de creativos en formato cuadrado listos para campañas de Meta Ads (Instagram Feed, Facebook Feed, Explorar y Marketplace) para el sistema **Finanzas 360**.

---

## 📁 Estructura de Carpetas

### 1. `creativos-meta/` (Carrusel Storytelling - Portadas y Secuencia)
- `card_1_fotografico.png`: **ANTES** (Recreación fotográfica realista de la referencia con 5 teléfonos, libreta y notas).
- `creativo_antes_manejar_vida.png`: "¿5 apps para manejar tu vida? Probá una." (1080x1080).
- `creativo_antes_ordenar_vida.png`: "¿5 apps para ordenar tu vida? Probá una." (1080x1080).
- `creativo_antes_finanzas.png`: "¿5 apps para tus finanzas? Probá una." (1080x1080).
- `creativo_antes_neutro.png`: "¿5 apps para manejar tu vida? Prueba una." (1080x1080).
- `card_1.png` a `card_7.png`: Secuencia vectorial / infográfica completa (1080x1080).
- `card_2.png`: **SIMPLIFICACIÓN** - Todo reemplazado por una sola planilla.
- `card_3.png`: **DESPUÉS** - Dashboard central y regla 50/30/20.
- `card_4.png`: **SIN SORPRESAS** - Módulo de cuotas y tarjetas con fecha fin.
- `card_5.png`: **AHORRO REAL** - Auditoría de gastos hormiga y suscripciones.
- `card_6.png`: **VISIÓN 360** - Meta de ahorro y fondo de emergencia proyectado.
- `card_7.png`: **OFERTA & CTA** - $9.900 ARS (70% OFF), un solo pago de por vida.

### 2. `creativos-meta/carrusel-producto/` (Carrusel de Producto & Hubs - 6 Tarjetas)
Secuencia estética mostrando cada área del producto:
- `prod_card_1.png`: Tu sistema financiero completo (Multidispositivo).
- `prod_card_2.png`: Todo en una sola planilla (Ecosistema 360).
- `prod_card_3.png`: Panel diario en 30 segundos (Foco & Claridad).
- `prod_card_4.png`: Cuotas, tarjetas y ahorro (Control Total).
- `prod_card_5.png`: Tus metas a 90 días, claras (Acción & Logros).
- `prod_card_6.png`: Hábitos, sueño y bienestar (Rutinas & Energía).

### 3. `creativos-meta/mockups-cuadrados/` (Mockups Puros 1080x1080)
Imágenes limpias centradas sobre fondo `#F5F3EC` con bordes suaves y sombra, sin textos publicitarios:
- `mockup_general_square.png`
- `gallery_overview_square.png`
- `gallery_dashboard_square.png`
- `gallery_finanzas_square.png`
- `gallery_metas_square.png`
- `gallery_bienestar_square.png`

---

## ⚙️ Regeneración de Creativos

Si necesitás modificar textos, colores o resoluciones:
- Para el carrusel narrativo: `python3 creativos-meta/generate_cards.py`
- Para el carrusel de producto y mockups: `python3 creativos-meta/generate_product_cards.py`
