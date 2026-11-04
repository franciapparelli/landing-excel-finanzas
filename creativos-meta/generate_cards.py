import os
import subprocess

OUTPUT_DIR = "/home/fran/Programming/landing-excel-finanzas/creativos-meta"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Common SVG styles and decorations
BG_COLOR = "#F5F3EC"
CARD_BG = "#FFFFFF"
TEXT_DARK = "#1E2229"
TEXT_MUTED = "#6B7280"
SAGE_BG = "#E3EAE4"
SAGE_TEXT = "#2C4F3B"
TERRA_BG = "#F7EBE4"
TERRA_TEXT = "#B85C38"
GREEN_ACCENT = "#10B981"
BORDER_COLOR = "#E6E2D8"

def get_base_svg(title, subtitle_tag, content_svg, slide_num=1):
    return f"""<svg width="1080" height="1080" viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="125%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="16" stdDeviation="24" flood-color="#000000" flood-opacity="0.08" />
    </filter>
    <filter id="subtle-shadow" x="-10%" y="-10%" width="120%" height="120%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.05" />
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1080" height="1080" fill="{BG_COLOR}" />

  <!-- Subtle organic background curves -->
  <path d="M-50,200 Q200,50 400,250 T800,100 T1150,300" fill="none" stroke="#EAE6DC" stroke-width="2" opacity="0.6"/>
  <path d="M-100,850 Q300,700 600,950 T1150,800" fill="none" stroke="#EAE6DC" stroke-width="2" opacity="0.6"/>
  <circle cx="950" cy="180" r="140" fill="#EFECE3" opacity="0.7"/>
  <circle cx="120" cy="920" r="160" fill="#EFECE3" opacity="0.7"/>

  <!-- Top Title -->
  <text x="540" y="150" font-family="'DejaVu Serif', Georgia, serif" font-size="46" font-weight="bold" fill="{TEXT_DARK}" text-anchor="middle" letter-spacing="-0.5">
    {title}
  </text>

  <!-- Subtitle Tag / Pill -->
  <g transform="translate(540, 195)">
    <rect x="-90" y="0" width="180" height="36" rx="18" fill="{SAGE_BG}"/>
    <text x="0" y="23" font-family="'DejaVu Sans', -apple-system, sans-serif" font-size="15" font-weight="600" fill="{SAGE_TEXT}" text-anchor="middle" letter-spacing="1">
      {subtitle_tag.upper()}
    </text>
  </g>

  <!-- Slide Number Dot Indicator -->
  <g transform="translate(540, 1010)">
    <rect x="-60" y="-18" width="120" height="30" rx="15" fill="#EAE5DC"/>
    <text x="0" y="2" font-family="'DejaVu Sans', sans-serif" font-size="14" font-weight="bold" fill="#78716C" text-anchor="middle">
      {slide_num} / 7
    </text>
  </g>

  <!-- Main Content Center -->
  {content_svg}
</svg>"""

cards = {}

# -------------------------------------------------------------
# CARD 1: ¿Tus finanzas en 5 lugares? Probá uno. (El caos del antes)
# -------------------------------------------------------------
card1_content = f"""
  <g transform="translate(140, 270)">
    <!-- Main Slate / Flatlay Card -->
    <rect width="800" height="670" rx="32" fill="{CARD_BG}" filter="url(#shadow)" stroke="{BORDER_COLOR}" stroke-width="2"/>
    
    <!-- Tag "ANTES" -->
    <rect x="50" y="45" width="85" height="30" rx="15" fill="#FEE2E2"/>
    <text x="92" y="65" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#DC2626" text-anchor="middle">ANTES</text>

    <!-- Post-it 1: Gastos sueltos -->
    <g transform="translate(80, 120) rotate(-4)">
      <rect width="200" height="180" rx="8" fill="#FEF08A" filter="url(#subtle-shadow)"/>
      <text x="25" y="45" font-family="'DejaVu Sans', sans-serif" font-size="15" font-weight="bold" fill="#854D0E">Compras mes:</text>
      <text x="25" y="80" font-family="'DejaVu Sans', sans-serif" font-size="14" fill="#A16207">• Luz: $34.000</text>
      <text x="25" y="110" font-family="'DejaVu Sans', sans-serif" font-size="14" fill="#A16207">• Super: ???</text>
      <text x="25" y="140" font-family="'DejaVu Sans', sans-serif" font-size="14" fill="#DC2626">• ¿Cuánto queda?</text>
    </g>

    <!-- Post-it 2: Cuotas de tarjeta -->
    <g transform="translate(520, 110) rotate(5)">
      <rect width="210" height="170" rx="8" fill="#FED7AA" filter="url(#subtle-shadow)"/>
      <text x="25" y="45" font-family="'DejaVu Sans', sans-serif" font-size="15" font-weight="bold" fill="#9A3412">Tarjeta Visa 💳</text>
      <text x="25" y="80" font-family="'DejaVu Sans', sans-serif" font-size="14" fill="#C2410C">Cierre: Jueves 24</text>
      <text x="25" y="110" font-family="'DejaVu Sans', sans-serif" font-size="14" fill="#C2410C">Cuotas: ¿4 de 6?</text>
      <text x="25" y="140" font-family="'DejaVu Sans', sans-serif" font-size="14" font-weight="bold" fill="#DC2626">Total: ¡Sorpresa!</text>
    </g>

    <!-- Smartphone Mockup in center -->
    <g transform="translate(285, 140)">
      <rect width="230" height="460" rx="36" fill="#18181B" filter="url(#shadow)"/>
      <rect x="8" y="8" width="214" height="444" rx="28" fill="#F4F4F5"/>
      <!-- Speaker & Camera -->
      <rect x="75" y="18" width="80" height="16" rx="8" fill="#18181B"/>
      
      <!-- Screen UI: 5 messy app icons -->
      <text x="115" y="70" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#52525B" text-anchor="middle">5 APPS SUELTAS</text>
      
      <!-- App 1: Bank app -->
      <g transform="translate(22, 95)">
        <rect width="170" height="52" rx="12" fill="#FFFFFF" stroke="#E4E4E7"/>
        <circle cx="28" cy="26" r="14" fill="#3B82F6"/>
        <text x="50" y="24" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#18181B">App del Banco</text>
        <text x="50" y="40" font-family="'DejaVu Sans', sans-serif" font-size="10" fill="#EF4444">Saldo en duda</text>
      </g>
      
      <!-- App 2: Notes -->
      <g transform="translate(22, 160)">
        <rect width="170" height="52" rx="12" fill="#FFFFFF" stroke="#E4E4E7"/>
        <circle cx="28" cy="26" r="14" fill="#EAB308"/>
        <text x="50" y="24" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#18181B">Notas del Celu</text>
        <text x="50" y="40" font-family="'DejaVu Sans', sans-serif" font-size="10" fill="#71717A">Desorden total</text>
      </g>

      <!-- App 3: WhatsApp with self -->
      <g transform="translate(22, 225)">
        <rect width="170" height="52" rx="12" fill="#FFFFFF" stroke="#E4E4E7"/>
        <circle cx="28" cy="26" r="14" fill="#22C55E"/>
        <text x="50" y="24" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#18181B">Chat conmigo</text>
        <text x="50" y="40" font-family="'DejaVu Sans', sans-serif" font-size="10" fill="#71717A">Audio de 2 min</text>
      </g>

      <!-- App 4: Dollar app subscription -->
      <g transform="translate(22, 290)">
        <rect width="170" height="52" rx="12" fill="#FFFFFF" stroke="#E4E4E7"/>
        <circle cx="28" cy="26" r="14" fill="#EC4899"/>
        <text x="50" y="24" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#18181B">App Finanzas</text>
        <text x="50" y="40" font-family="'DejaVu Sans', sans-serif" font-size="10" fill="#DC2626">$4.99 USD/mes</text>
      </g>
      
      <!-- Warning box bottom -->
      <rect x="22" y="360" width="170" height="42" rx="10" fill="#FEE2E2"/>
      <text x="107" y="386" font-family="'DejaVu Sans', sans-serif" font-size="11" font-weight="bold" fill="#B91C1C" text-anchor="middle">❌ Cero previsión</text>
    </g>

    <!-- Post-it 3: Fin de mes -->
    <g transform="translate(85, 390) rotate(3)">
      <rect width="180" height="150" rx="8" fill="#E0E7FF" filter="url(#subtle-shadow)"/>
      <text x="20" y="40" font-family="'DejaVu Sans', sans-serif" font-size="14" font-weight="bold" fill="#3730A3">Día 20 del mes:</text>
      <text x="20" y="75" font-family="'DejaVu Sans', sans-serif" font-size="13" fill="#4338CA">"¿A dónde se me</text>
      <text x="20" y="100" font-family="'DejaVu Sans', sans-serif" font-size="13" fill="#4338CA">fue la plata?" 🤦‍♂️</text>
    </g>

    <!-- Post-it 4: Cuaderno -->
    <g transform="translate(535, 370) rotate(-3)">
      <rect width="190" height="160" rx="8" fill="#FCE7F3" filter="url(#subtle-shadow)"/>
      <text x="20" y="40" font-family="'DejaVu Sans', sans-serif" font-size="14" font-weight="bold" fill="#9D174D">Anotador papel</text>
      <text x="20" y="75" font-family="'DejaVu Sans', sans-serif" font-size="13" fill="#BE185D">Lo abrís 3 días</text>
      <text x="20" y="100" font-family="'DejaVu Sans', sans-serif" font-size="13" fill="#BE185D">y lo dejás tirado</text>
    </g>
  </g>
"""
cards[1] = get_base_svg("¿Tus finanzas en 5 lugares? Probá uno.", "antes", card1_content, 1)

# -------------------------------------------------------------
# CARD 2: Reemplazado por una sola planilla (Diagrama de Stack)
# -------------------------------------------------------------
card2_content = f"""
  <g transform="translate(130, 270)">
    <!-- Container Card -->
    <rect width="820" height="670" rx="32" fill="{CARD_BG}" filter="url(#shadow)" stroke="{BORDER_COLOR}" stroke-width="2"/>

    <!-- Left Box: The replaced stack -->
    <g transform="translate(50, 70)">
      <rect width="320" height="530" rx="24" fill="#FAF8F5" stroke="#E6E0D6" stroke-width="2" />
      <text x="160" y="55" font-family="'DejaVu Sans', sans-serif" font-size="16" font-weight="bold" fill="#78716C" text-anchor="middle">REEMPLAZA TODO ESTO:</text>

      <!-- Strikethrough item 1 -->
      <g transform="translate(25, 90)">
        <rect width="270" height="60" rx="12" fill="#FFFFFF" stroke="#E7E5E4"/>
        <text x="20" y="36" font-family="'DejaVu Sans', sans-serif" font-size="15" fill="#A8A29E" text-decoration="line-through">~Bloc de notas~</text>
      </g>

      <!-- Strikethrough item 2 -->
      <g transform="translate(25, 170)">
        <rect width="270" height="60" rx="12" fill="#FFFFFF" stroke="#E7E5E4"/>
        <text x="20" y="36" font-family="'DejaVu Sans', sans-serif" font-size="15" fill="#A8A29E" text-decoration="line-through">~App en USD ($4.99/mes)~</text>
      </g>

      <!-- Strikethrough item 3 -->
      <g transform="translate(25, 250)">
        <rect width="270" height="60" rx="12" fill="#FFFFFF" stroke="#E7E5E4"/>
        <text x="20" y="36" font-family="'DejaVu Sans', sans-serif" font-size="15" fill="#A8A29E" text-decoration="line-through">~Chat de WhatsApp solo~</text>
      </g>

      <!-- Strikethrough item 4 -->
      <g transform="translate(25, 330)">
        <rect width="270" height="60" rx="12" fill="#FFFFFF" stroke="#E7E5E4"/>
        <text x="20" y="36" font-family="'DejaVu Sans', sans-serif" font-size="15" fill="#A8A29E" text-decoration="line-through">~Sorpresa de la tarjeta~</text>
      </g>

      <!-- Strikethrough item 5 -->
      <g transform="translate(25, 410)">
        <rect width="270" height="60" rx="12" fill="#FFFFFF" stroke="#E7E5E4"/>
        <text x="20" y="36" font-family="'DejaVu Sans', sans-serif" font-size="15" fill="#A8A29E" text-decoration="line-through">~Cuaderno de papel~</text>
      </g>
      
      <!-- Badge "-5 herramientas" -->
      <g transform="translate(90, 485)">
        <rect width="140" height="32" rx="16" fill="#FEE2E2"/>
        <text x="70" y="21" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#DC2626" text-anchor="middle">- 5 HERRAMIENTAS</text>
      </g>
    </g>

    <!-- Arrow in Middle -->
    <g transform="translate(385, 315)">
      <circle cx="25" cy="20" r="28" fill="#F3EFEA"/>
      <path d="M12,20 L36,20 M26,10 L38,20 L26,30" stroke="#2C4F3B" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
    </g>

    <!-- Right Box: One Google Sheets Template -->
    <g transform="translate(450, 70)">
      <rect width="320" height="530" rx="24" fill="{SAGE_BG}" stroke="#BCD0C0" stroke-width="2" />
      
      <!-- Icon Sheets -->
      <g transform="translate(130, 50)">
        <rect width="60" height="70" rx="10" fill="#0F9D58"/>
        <!-- Sheet lines -->
        <rect x="12" y="22" width="36" height="6" fill="#FFFFFF"/>
        <rect x="12" y="34" width="36" height="6" fill="#FFFFFF"/>
        <rect x="12" y="46" width="36" height="6" fill="#FFFFFF"/>
      </g>

      <text x="160" y="165" font-family="'DejaVu Serif', serif" font-size="28" font-weight="bold" fill="{TEXT_DARK}" text-anchor="middle">Finanzas 360</text>
      <text x="160" y="195" font-family="'DejaVu Sans', sans-serif" font-size="14" font-weight="600" fill="{SAGE_TEXT}" text-anchor="middle">Google Sheets + Excel</text>

      <!-- Checklist -->
      <g transform="translate(30, 230)">
        <circle cx="15" cy="15" r="12" fill="#2C4F3B"/>
        <path d="M10,15 L14,19 L20,11" stroke="#FFFFFF" stroke-width="2.5" fill="none"/>
        <text x="36" y="20" font-family="'DejaVu Sans', sans-serif" font-size="14" font-weight="bold" fill="{TEXT_DARK}">Un solo panel central</text>
      </g>

      <g transform="translate(30, 290)">
        <circle cx="15" cy="15" r="12" fill="#2C4F3B"/>
        <path d="M10,15 L14,19 L20,11" stroke="#FFFFFF" stroke-width="2.5" fill="none"/>
        <text x="36" y="20" font-family="'DejaVu Sans', sans-serif" font-size="14" font-weight="bold" fill="{TEXT_DARK}">Cuotas y tarjetas al día</text>
      </g>

      <g transform="translate(30, 350)">
        <circle cx="15" cy="15" r="12" fill="#2C4F3B"/>
        <path d="M10,15 L14,19 L20,11" stroke="#FFFFFF" stroke-width="2.5" fill="none"/>
        <text x="36" y="20" font-family="'DejaVu Sans', sans-serif" font-size="14" font-weight="bold" fill="{TEXT_DARK}">Solo 10 min por semana</text>
      </g>

      <g transform="translate(30, 410)">
        <circle cx="15" cy="15" r="12" fill="#2C4F3B"/>
        <path d="M10,15 L14,19 L20,11" stroke="#FFFFFF" stroke-width="2.5" fill="none"/>
        <text x="36" y="20" font-family="'DejaVu Sans', sans-serif" font-size="14" font-weight="bold" fill="{TEXT_DARK}">100% automatizado</text>
      </g>

      <!-- Badge "1 solo pago" -->
      <g transform="translate(65, 475)">
        <rect width="190" height="34" rx="17" fill="#2C4F3B"/>
        <text x="95" y="22" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">UN SOLO PAGO · $9.900</text>
      </g>
    </g>
  </g>
"""
cards[2] = get_base_svg("Reemplazado por una sola planilla", "simplificación", card2_content, 2)

# -------------------------------------------------------------
# CARD 3: Un panel central para todo tu mes (Dashboard Mockup)
# -------------------------------------------------------------
card3_content = f"""
  <g transform="translate(130, 260)">
    <!-- Tablet Bezel -->
    <rect width="820" height="690" rx="36" fill="#18181B" filter="url(#shadow)"/>
    <rect x="14" y="14" width="792" height="662" rx="26" fill="#F8FAFC"/>
    
    <!-- Top Tablet Camera -->
    <circle cx="410" cy="24" r="4" fill="#3F3F46"/>

    <!-- Inside Tablet Screen -->
    <g transform="translate(30, 45)">
      <!-- Spreadsheet Top Bar -->
      <rect width="760" height="42" rx="8" fill="#FFFFFF" stroke="#E2E8F0"/>
      <circle cx="20" cy="21" r="5" fill="#EF4444"/>
      <circle cx="36" cy="21" r="5" fill="#EAB308"/>
      <circle cx="52" cy="21" r="5" fill="#10B981"/>
      <text x="75" y="26" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#0F172A">Control_Financiero_2026.xlsx</text>
      <rect x="620" y="9" width="125" height="24" rx="6" fill="#ECFDF5"/>
      <text x="682" y="25" font-family="'DejaVu Sans', sans-serif" font-size="10" font-weight="bold" fill="#059669" text-anchor="middle">● EN LÍNEA / AUTO</text>

      <!-- Row of 3 KPI Cards -->
      <g transform="translate(0, 58)">
        <!-- KPI 1 -->
        <rect x="0" width="242" height="110" rx="14" fill="#FFFFFF" stroke="#E2E8F0" filter="url(#subtle-shadow)"/>
        <text x="18" y="32" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#64748B">INGRESOS DEL MES</text>
        <text x="18" y="68" font-family="'DejaVu Sans', sans-serif" font-size="22" font-weight="bold" fill="#0F172A">$ 1.480.000</text>
        <text x="18" y="92" font-family="'DejaVu Sans', sans-serif" font-size="11" font-weight="bold" fill="#10B981">▲ Sueldo + Extras</text>

        <!-- KPI 2 -->
        <rect x="258" width="242" height="110" rx="14" fill="#FFFFFF" stroke="#E2E8F0" filter="url(#subtle-shadow)"/>
        <text x="276" y="32" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#64748B">GASTOS TOTALES</text>
        <text x="276" y="68" font-family="'DejaVu Sans', sans-serif" font-size="22" font-weight="bold" fill="#0F172A">$ 1.155.500</text>
        <text x="276" y="92" font-family="'DejaVu Sans', sans-serif" font-size="11" font-weight="bold" fill="#64748B">Fijos + Cuotas + Variables</text>

        <!-- KPI 3: Ahorro -->
        <rect x="518" width="242" height="110" rx="14" fill="#ECFDF5" stroke="#A7F3D0" filter="url(#subtle-shadow)"/>
        <text x="536" y="32" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#047857">AHORRO DISPONIBLE</text>
        <text x="536" y="68" font-family="'DejaVu Sans', sans-serif" font-size="24" font-weight="bold" fill="#047857">$ 324.500</text>
        <text x="536" y="92" font-family="'DejaVu Sans', sans-serif" font-size="11" font-weight="bold" fill="#059669">✓ 22% del ingreso mensual</text>
      </g>

      <!-- Section: Regla 50 / 30 / 20 -->
      <g transform="translate(0, 185)">
        <rect width="760" height="135" rx="14" fill="#FFFFFF" stroke="#E2E8F0"/>
        <text x="20" y="32" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#1E293B">DISTRIBUCIÓN SUGERIDA (MÉTODO 50/30/20)</text>
        
        <!-- Multi-bar -->
        <g transform="translate(20, 50)">
          <rect width="360" height="34" rx="8" fill="#10B981"/>
          <text x="180" y="22" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">50% Necesidades ($740k)</text>
          
          <rect x="366" width="220" height="34" rx="8" fill="#3B82F6"/>
          <text x="476" y="22" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">30% Estilo ($444k)</text>
          
          <rect x="592" width="128" height="34" rx="8" fill="#F59E0B"/>
          <text x="656" y="22" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">20% Ahorro</text>
        </g>
        <text x="20" y="115" font-family="'DejaVu Sans', sans-serif" font-size="11" fill="#64748B">Las fórmulas calculan si estás dentro de tu límite seguro para no endeudarte.</text>
      </g>

      <!-- Section: Balance Anual Visual Preview -->
      <g transform="translate(0, 335)">
        <rect width="760" height="235" rx="14" fill="#FFFFFF" stroke="#E2E8F0"/>
        <text x="20" y="32" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#1E293B">EVOLUCIÓN MES A MES (ENERO - DICIEMBRE)</text>
        
        <!-- Simulated Bar Chart -->
        <g transform="translate(30, 60)">
          <!-- Month Bars (Ene to Jun) -->
          <rect x="20" y="70" width="35" height="100" rx="4" fill="#CBD5E1"/>
          <rect x="20" y="30" width="35" height="40" rx="4" fill="#10B981"/>
          <text x="37" y="190" font-family="'DejaVu Sans', sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Ene</text>

          <rect x="100" y="65" width="35" height="105" rx="4" fill="#CBD5E1"/>
          <rect x="100" y="20" width="35" height="45" rx="4" fill="#10B981"/>
          <text x="117" y="190" font-family="'DejaVu Sans', sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Feb</text>

          <rect x="180" y="60" width="35" height="110" rx="4" fill="#CBD5E1"/>
          <rect x="180" y="15" width="35" height="45" rx="4" fill="#10B981"/>
          <text x="197" y="190" font-family="'DejaVu Sans', sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Mar</text>

          <rect x="260" y="55" width="35" height="115" rx="4" fill="#CBD5E1"/>
          <rect x="260" y="10" width="35" height="45" rx="4" fill="#10B981"/>
          <text x="277" y="190" font-family="'DejaVu Sans', sans-serif" font-size="11" fill="#64748B" text-anchor="middle">Abr</text>

          <rect x="340" y="50" width="35" height="120" rx="4" fill="#CBD5E1"/>
          <rect x="340" y="5" width="35" height="45" rx="4" fill="#10B981"/>
          <text x="357" y="190" font-family="'DejaVu Sans', sans-serif" font-size="11" fill="#64748B" text-anchor="middle">May</text>

          <!-- Legend Box -->
          <g transform="translate(430, 20)">
            <rect width="260" height="140" rx="10" fill="#F8FAFC" stroke="#E2E8F0"/>
            <circle cx="25" cy="35" r="7" fill="#10B981"/>
            <text x="42" y="40" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#0F172A">Ahorro acumulado</text>
            
            <circle cx="25" cy="70" r="7" fill="#CBD5E1"/>
            <text x="42" y="75" font-family="'DejaVu Sans', sans-serif" font-size="12" fill="#64748B">Gastos controlados</text>

            <rect x="20" y="95" width="220" height="30" rx="6" fill="#ECFDF5"/>
            <text x="130" y="115" font-family="'DejaVu Sans', sans-serif" font-size="11" font-weight="bold" fill="#047857" text-anchor="middle">Meta Anual: 78% alcanzada</text>
          </g>
        </g>
      </g>
    </g>
  </g>
"""
cards[3] = get_base_svg("Un panel central para todo tu mes", "después", card3_content, 3)

# -------------------------------------------------------------
# CARD 4: Tus cuotas y tarjetas, bajo control (Módulo de Cuotas)
# -------------------------------------------------------------
card4_content = f"""
  <g transform="translate(130, 260)">
    <!-- Tablet Bezel -->
    <rect width="820" height="690" rx="36" fill="#18181B" filter="url(#shadow)"/>
    <rect x="14" y="14" width="792" height="662" rx="26" fill="#F8FAFC"/>
    
    <!-- Top Tablet Camera -->
    <circle cx="410" cy="24" r="4" fill="#3F3F46"/>

    <g transform="translate(30, 45)">
      <!-- Tab Header -->
      <rect width="760" height="50" rx="10" fill="#FFFFFF" stroke="#E2E8F0"/>
      <text x="25" y="32" font-family="'DejaVu Sans', sans-serif" font-size="15" font-weight="bold" fill="#0F172A">💳 MÓDULO DE TARJETAS Y CUOTAS FUTURAS</text>
      <rect x="580" y="11" width="160" height="28" rx="6" fill="#EFF6FF"/>
      <text x="660" y="30" font-family="'DejaVu Sans', sans-serif" font-size="11" font-weight="bold" fill="#2563EB" text-anchor="middle">PREVISIÓN EXACTA</text>

      <!-- Alert Banner: Total próximo resumen -->
      <g transform="translate(0, 65)">
        <rect width="760" height="85" rx="14" fill="#FEF3C7" stroke="#FDE68A"/>
        <text x="25" y="35" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#92400E">TOTAL A PAGAR EN EL PRÓXIMO RESUMEN (CIERRE 25):</text>
        <text x="25" y="70" font-family="'DejaVu Sans', sans-serif" font-size="28" font-weight="bold" fill="#B45309">$ 189.400 ARS</text>
        <rect x="540" y="24" width="195" height="38" rx="8" fill="#FFFFFF" stroke="#FCD34D"/>
        <text x="637" y="48" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#92400E" text-anchor="middle">✓ Cubierto por sueldo</text>
      </g>

      <!-- Installment Table -->
      <g transform="translate(0, 165)">
        <rect width="760" height="400" rx="14" fill="#FFFFFF" stroke="#E2E8F0"/>
        
        <!-- Table Header -->
        <rect width="760" height="44" rx="10" fill="#F1F5F9"/>
        <text x="25" y="28" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#475569">COMPRA / DETALLE</text>
        <text x="260" y="28" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#475569">TOTAL</text>
        <text x="380" y="28" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#475569">CUOTA</text>
        <text x="490" y="28" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#475569">VALOR MES</text>
        <text x="640" y="28" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#475569">FINALIZA EN</text>

        <!-- Row 1 -->
        <line x1="0" y1="95" x2="760" y2="95" stroke="#F1F5F9" stroke-width="1.5"/>
        <text x="25" y="75" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#0F172A">Notebook Trabajo</text>
        <text x="260" y="75" font-family="'DejaVu Sans', sans-serif" font-size="13" fill="#64748B">$ 480.000</text>
        <rect x="380" y="56" width="60" height="26" rx="6" fill="#E2E8F0"/>
        <text x="410" y="74" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#334155" text-anchor="middle">4 / 6</text>
        <text x="490" y="75" font-family="'DejaVu Sans', sans-serif" font-size="14" font-weight="bold" fill="#0F172A">$ 80.000</text>
        <text x="640" y="75" font-family="'DejaVu Sans', sans-serif" font-size="12" fill="#059669">Mayo 2026</text>

        <!-- Row 2 -->
        <line x1="0" y1="150" x2="760" y2="150" stroke="#F1F5F9" stroke-width="1.5"/>
        <text x="25" y="130" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#0F172A">Zapatillas Running</text>
        <text x="260" y="130" font-family="'DejaVu Sans', sans-serif" font-size="13" fill="#64748B">$ 120.000</text>
        <rect x="380" y="111" width="60" height="26" rx="6" fill="#E2E8F0"/>
        <text x="410" y="129" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#334155" text-anchor="middle">2 / 3</text>
        <text x="490" y="130" font-family="'DejaVu Sans', sans-serif" font-size="14" font-weight="bold" fill="#0F172A">$ 40.000</text>
        <text x="640" y="130" font-family="'DejaVu Sans', sans-serif" font-size="12" fill="#059669">Abril 2026</text>

        <!-- Row 3 -->
        <line x1="0" y1="205" x2="760" y2="205" stroke="#F1F5F9" stroke-width="1.5"/>
        <text x="25" y="185" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#0F172A">Pasajes Vacaciones</text>
        <text x="260" y="185" font-family="'DejaVu Sans', sans-serif" font-size="13" fill="#64748B">$ 340.000</text>
        <rect x="380" y="166" width="60" height="26" rx="6" fill="#E2E8F0"/>
        <text x="410" y="184" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#334155" text-anchor="middle">5 / 10</text>
        <text x="490" y="185" font-family="'DejaVu Sans', sans-serif" font-size="14" font-weight="bold" fill="#0F172A">$ 34.000</text>
        <text x="640" y="185" font-family="'DejaVu Sans', sans-serif" font-size="12" fill="#059669">Agosto 2026</text>

        <!-- Row 4 -->
        <line x1="0" y1="260" x2="760" y2="260" stroke="#F1F5F9" stroke-width="1.5"/>
        <text x="25" y="240" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#0F172A">Curso Online</text>
        <text x="260" y="240" font-family="'DejaVu Sans', sans-serif" font-size="13" fill="#64748B">$ 70.800</text>
        <rect x="380" y="221" width="60" height="26" rx="6" fill="#E2E8F0"/>
        <text x="410" y="239" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#334155" text-anchor="middle">2 / 2</text>
        <text x="490" y="240" font-family="'DejaVu Sans', sans-serif" font-size="14" font-weight="bold" fill="#0F172A">$ 35.400</text>
        <text x="640" y="240" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#10B981">¡Última cuota!</text>

        <!-- Bottom Highlight Box inside Table -->
        <g transform="translate(20, 285)">
          <rect width="720" height="90" rx="10" fill="#ECFDF5" stroke="#A7F3D0"/>
          <text x="20" y="32" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#047857">PROYECCIÓN DE ALIVIO FINANCIERO:</text>
          <text x="20" y="62" font-family="'DejaVu Sans', sans-serif" font-size="14" fill="#065F46">En 2 meses se liberan $75.400 mensuales al terminar cuotas pendientes.</text>
        </g>
      </g>
    </g>
  </g>
"""
cards[4] = get_base_svg("Tus cuotas y tarjetas, bajo control", "sin sorpresas", card4_content, 4)

# -------------------------------------------------------------
# CARD 5: Tus gastos hormiga, detectados
# -------------------------------------------------------------
card5_content = f"""
  <g transform="translate(130, 260)">
    <!-- Tablet Bezel -->
    <rect width="820" height="690" rx="36" fill="#18181B" filter="url(#shadow)"/>
    <rect x="14" y="14" width="792" height="662" rx="26" fill="#F8FAFC"/>
    
    <!-- Top Tablet Camera -->
    <circle cx="410" cy="24" r="4" fill="#3F3F46"/>

    <g transform="translate(30, 45)">
      <!-- Tab Header -->
      <rect width="760" height="50" rx="10" fill="#FFFFFF" stroke="#E2E8F0"/>
      <text x="25" y="32" font-family="'DejaVu Sans', sans-serif" font-size="15" font-weight="bold" fill="#0F172A">🔍 AUDITORÍA DE FUGAS &amp; GASTOS HORMIGA</text>
      <rect x="580" y="11" width="160" height="28" rx="6" fill="#FEE2E2"/>
      <text x="660" y="30" font-family="'DejaVu Sans', sans-serif" font-size="11" font-weight="bold" fill="#DC2626" text-anchor="middle">FUGA DETECTADA</text>

      <!-- Big Red Banner -->
      <g transform="translate(0, 65)">
        <rect width="760" height="95" rx="14" fill="#FEF2F2" stroke="#FECACA"/>
        <text x="25" y="35" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#991B1B">GASTOS HORMIGA &amp; SUSCRIPCIONES NO USADAS DETECTADAS:</text>
        <text x="25" y="74" font-family="'DejaVu Sans', sans-serif" font-size="30" font-weight="bold" fill="#DC2626">$ 48.200 ARS / mes</text>
        <rect x="520" y="28" width="215" height="42" rx="8" fill="#FFFFFF" stroke="#FCA5A5"/>
        <text x="627" y="54" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#B91C1C" text-anchor="middle">❌ $ 578.400 / año</text>
      </g>

      <!-- Detected Subscriptions List -->
      <g transform="translate(0, 180)">
        <rect width="760" height="385" rx="14" fill="#FFFFFF" stroke="#E2E8F0"/>
        
        <text x="25" y="36" font-family="'DejaVu Sans', sans-serif" font-size="14" font-weight="bold" fill="#0F172A">Gastos prescindibles detectados automáticamente:</text>

        <!-- Item 1 -->
        <g transform="translate(25, 55)">
          <rect width="710" height="60" rx="10" fill="#F8FAFC" stroke="#E2E8F0"/>
          <circle cx="30" cy="30" r="14" fill="#FEE2E2"/>
          <text x="30" y="35" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#DC2626" text-anchor="middle">✕</text>
          <text x="60" y="28" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#1E293B">App de streaming olvidada (débito auto)</text>
          <text x="60" y="46" font-family="'DejaVu Sans', sans-serif" font-size="11" fill="#64748B">Sin uso en los últimos 90 días</text>
          <text x="590" y="36" font-family="'DejaVu Sans', sans-serif" font-size="15" font-weight="bold" fill="#DC2626">$ 8.200 / mes</text>
        </g>

        <!-- Item 2 -->
        <g transform="translate(25, 125)">
          <rect width="710" height="60" rx="10" fill="#F8FAFC" stroke="#E2E8F0"/>
          <circle cx="30" cy="30" r="14" fill="#FEE2E2"/>
          <text x="30" y="35" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#DC2626" text-anchor="middle">✕</text>
          <text x="60" y="28" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#1E293B">Membresía premium inactiva</text>
          <text x="60" y="46" font-family="'DejaVu Sans', sans-serif" font-size="11" fill="#64748B">Cobro recurrente sin aprovechamiento</text>
          <text x="590" y="36" font-family="'DejaVu Sans', sans-serif" font-size="15" font-weight="bold" fill="#DC2626">$ 14.500 / mes</text>
        </g>

        <!-- Item 3 -->
        <g transform="translate(25, 195)">
          <rect width="710" height="60" rx="10" fill="#F8FAFC" stroke="#E2E8F0"/>
          <circle cx="30" cy="30" r="14" fill="#FEE2E2"/>
          <text x="30" y="35" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#DC2626" text-anchor="middle">✕</text>
          <text x="60" y="28" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#1E293B">Deliverys no planificados (fines de semana)</text>
          <text x="60" y="46" font-family="'DejaVu Sans', sans-serif" font-size="11" fill="#64748B">Supera el tope de la categoría ocio</text>
          <text x="590" y="36" font-family="'DejaVu Sans', sans-serif" font-size="15" font-weight="bold" fill="#DC2626">$ 25.500 / mes</text>
        </g>

        <!-- Green Solution Banner -->
        <g transform="translate(25, 275)">
          <rect width="710" height="85" rx="12" fill="#ECFDF5" stroke="#A7F3D0"/>
          <text x="25" y="34" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#047857">💡 RETORNO INMEDIATO DE TU INVERSIÓN:</text>
          <text x="25" y="60" font-family="'DejaVu Sans', sans-serif" font-size="14" fill="#065F46">Cancelando solo una de estas suscripciones, recuperás los $9.900 de la planilla en tu primera semana.</text>
        </g>
      </g>
    </g>
  </g>
"""
cards[5] = get_base_svg("Tus gastos hormiga, detectados", "ahorro real", card5_content, 5)

# -------------------------------------------------------------
# CARD 6: Tu meta de ahorro, proyectada (Metas & Fondo de emergencia)
# -------------------------------------------------------------
card6_content = f"""
  <g transform="translate(130, 260)">
    <!-- Tablet Bezel -->
    <rect width="820" height="690" rx="36" fill="#18181B" filter="url(#shadow)"/>
    <rect x="14" y="14" width="792" height="662" rx="26" fill="#F8FAFC"/>
    
    <!-- Top Tablet Camera -->
    <circle cx="410" cy="24" r="4" fill="#3F3F46"/>

    <g transform="translate(30, 45)">
      <!-- Tab Header -->
      <rect width="760" height="50" rx="10" fill="#FFFFFF" stroke="#E2E8F0"/>
      <text x="25" y="32" font-family="'DejaVu Sans', sans-serif" font-size="15" font-weight="bold" fill="#0F172A">🎯 PLANIFICADOR DE METAS &amp; FONDO DE EMERGENCIA</text>
      <rect x="580" y="11" width="160" height="28" rx="6" fill="#ECFDF5"/>
      <text x="660" y="30" font-family="'DejaVu Sans', sans-serif" font-size="11" font-weight="bold" fill="#059669" text-anchor="middle">CRECIMIENTO REAL</text>

      <!-- Goal Card 1: Fondo de Emergencia -->
      <g transform="translate(0, 65)">
        <rect width="760" height="150" rx="14" fill="#FFFFFF" stroke="#E2E8F0" filter="url(#subtle-shadow)"/>
        <text x="25" y="35" font-family="'DejaVu Sans', sans-serif" font-size="15" font-weight="bold" fill="#0F172A">Meta 1: Fondo de Emergencia (3 meses de gastos fijos)</text>
        <text x="25" y="65" font-family="'DejaVu Sans', sans-serif" font-size="13" fill="#64748B">Objetivo: $ 1.800.000 ARS  •  Ahorrado: <tspan font-weight="bold" fill="#10B981">$ 1.250.000 ARS</tspan></text>
        
        <!-- Progress Bar -->
        <rect x="25" y="85" width="710" height="22" rx="11" fill="#E2E8F0"/>
        <rect x="25" y="85" width="495" height="22" rx="11" fill="#10B981"/>
        <text x="560" y="102" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#047857">70% COMPLETADO</text>
        
        <text x="25" y="132" font-family="'DejaVu Sans', sans-serif" font-size="11" fill="#059669">✓ Faltan solo 2 meses manteniendo tu ritmo actual de ahorro.</text>
      </g>

      <!-- Goal Card 2: Vacaciones / Viaje -->
      <g transform="translate(0, 230)">
        <rect width="760" height="150" rx="14" fill="#FFFFFF" stroke="#E2E8F0" filter="url(#subtle-shadow)"/>
        <text x="25" y="35" font-family="'DejaVu Sans', sans-serif" font-size="15" font-weight="bold" fill="#0F172A">Meta 2: Viaje a la Costa / Vacaciones de Invierno</text>
        <text x="25" y="65" font-family="'DejaVu Sans', sans-serif" font-size="13" fill="#64748B">Objetivo: $ 600.000 ARS  •  Ahorrado: <tspan font-weight="bold" fill="#3B82F6">$ 510.000 ARS</tspan></text>
        
        <!-- Progress Bar -->
        <rect x="25" y="85" width="710" height="22" rx="11" fill="#E2E8F0"/>
        <rect x="25" y="85" width="600" height="22" rx="11" fill="#3B82F6"/>
        <text x="645" y="102" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#1E40AF">85%</text>

        <text x="25" y="132" font-family="'DejaVu Sans', sans-serif" font-size="11" fill="#2563EB">✓ En objetivo para viajar sin tener que tarjetear todo a último momento.</text>
      </g>

      <!-- Bottom Motivation Quote -->
      <g transform="translate(0, 395)">
        <rect width="760" height="150" rx="14" fill="{SAGE_BG}" stroke="#BCD0C0"/>
        <text x="380" y="45" font-family="'DejaVu Serif', serif" font-size="20" font-weight="bold" fill="{TEXT_DARK}" text-anchor="middle">"El dinero ordenado compra tranquilidad."</text>
        <text x="380" y="80" font-family="'DejaVu Sans', sans-serif" font-size="14" fill="{SAGE_TEXT}" text-anchor="middle">No necesitás ganar el doble para empezar a ahorrar.</text>
        <text x="380" y="110" font-family="'DejaVu Sans', sans-serif" font-size="14" font-weight="bold" fill="{TEXT_DARK}" text-anchor="middle">Solo necesitás un sistema que te muestre la verdad de tus números.</text>
      </g>
    </g>
  </g>
"""
cards[6] = get_base_svg("Tu meta de ahorro, proyectada", "visión 360", card6_content, 6)

# -------------------------------------------------------------
# CARD 7: Todo tu año ordenado por $9.900 (Oferta final y CTA)
# -------------------------------------------------------------
card7_content = f"""
  <g transform="translate(130, 260)">
    <!-- Main Outer Card -->
    <rect width="820" height="690" rx="36" fill="{CARD_BG}" filter="url(#shadow)" stroke="{BORDER_COLOR}" stroke-width="2"/>

    <!-- Offer Ribbon Top -->
    <g transform="translate(260, 25)">
      <rect width="300" height="34" rx="17" fill="#FEF3C7" stroke="#FDE68A"/>
      <text x="150" y="23" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#92400E" text-anchor="middle">⚡ ACCESO COMPLETO E INMEDIATO</text>
    </g>

    <!-- Main Title of Product -->
    <text x="410" y="105" font-family="'DejaVu Serif', serif" font-size="34" font-weight="bold" fill="{TEXT_DARK}" text-anchor="middle">Sistema Finanzas360</text>
    <text x="410" y="135" font-family="'DejaVu Sans', sans-serif" font-size="16" fill="{TEXT_MUTED}" text-anchor="middle">Plantilla Google Sheets + Excel + Guía en PDF descargable</text>

    <!-- Feature Pills Grid -->
    <g transform="translate(60, 160)">
      <!-- Pill 1 -->
      <g transform="translate(0, 0)">
        <rect width="335" height="50" rx="12" fill="#F8FAFC" stroke="#E2E8F0"/>
        <circle cx="28" cy="25" r="12" fill="#10B981"/>
        <text x="28" y="30" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">✓</text>
        <text x="52" y="31" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#1E293B">Google Drive 100% Gratis</text>
      </g>
      <!-- Pill 2 -->
      <g transform="translate(365, 0)">
        <rect width="335" height="50" rx="12" fill="#F8FAFC" stroke="#E2E8F0"/>
        <circle cx="28" cy="25" r="12" fill="#10B981"/>
        <text x="28" y="30" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">✓</text>
        <text x="52" y="31" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#1E293B">Apto Celular, Tablet y PC</text>
      </g>
      <!-- Pill 3 -->
      <g transform="translate(0, 62)">
        <rect width="335" height="50" rx="12" fill="#F8FAFC" stroke="#E2E8F0"/>
        <circle cx="28" cy="25" r="12" fill="#10B981"/>
        <text x="28" y="30" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">✓</text>
        <text x="52" y="31" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#1E293B">Módulo Cuotas &amp; Tarjetas</text>
      </g>
      <!-- Pill 4 -->
      <g transform="translate(365, 62)">
        <rect width="335" height="50" rx="12" fill="#F8FAFC" stroke="#E2E8F0"/>
        <circle cx="28" cy="25" r="12" fill="#10B981"/>
        <text x="28" y="30" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">✓</text>
        <text x="52" y="31" font-family="'DejaVu Sans', sans-serif" font-size="13" font-weight="bold" fill="#1E293B">Sin cuotas mensuales en USD</text>
      </g>
    </g>

    <!-- Pricing Box Center -->
    <g transform="translate(60, 295)">
      <rect width="700" height="210" rx="20" fill="#FAF8F5" stroke="#E6E0D6" stroke-width="2"/>
      
      <!-- Strikethrough regular price -->
      <text x="350" y="45" font-family="'DejaVu Sans', sans-serif" font-size="16" fill="#A8A29E" text-anchor="middle">
        Precio regular: <tspan text-decoration="line-through">$35.000 ARS</tspan>
      </text>

      <!-- Discount badge -->
      <rect x="490" y="27" width="95" height="26" rx="13" fill="#FEE2E2"/>
      <text x="537" y="45" font-family="'DejaVu Sans', sans-serif" font-size="12" font-weight="bold" fill="#DC2626" text-anchor="middle">70% OFF</text>

      <!-- Main Price Big -->
      <text x="350" y="125" font-family="'DejaVu Sans', sans-serif" font-size="64" font-weight="bold" fill="{TEXT_DARK}" text-anchor="middle">
        $ 9.900 <tspan font-size="24" fill="#78716C">ARS</tspan>
      </text>

      <text x="350" y="165" font-family="'DejaVu Sans', sans-serif" font-size="14" font-weight="bold" fill="{SAGE_TEXT}" text-anchor="middle">
        UN SOLO PAGO DE POR VIDA · SIN SUSCRIPCIONES
      </text>

      <text x="350" y="190" font-family="'DejaVu Sans', sans-serif" font-size="12" fill="#78716C" text-anchor="middle">
        Descarga automática a tu correo electrónico al instante
      </text>
    </g>

    <!-- CTA Button Bottom -->
    <g transform="translate(130, 535)">
      <rect width="560" height="70" rx="16" fill="#009EE3" filter="url(#shadow)"/>
      <text x="280" y="44" font-family="'DejaVu Sans', sans-serif" font-size="20" font-weight="bold" fill="#FFFFFF" text-anchor="middle">
        OBTENER EL SISTEMA AHORA →
      </text>
    </g>

    <!-- Guarantee & Security Subtext -->
    <text x="410" y="645" font-family="'DejaVu Sans', sans-serif" font-size="12" fill="#78716C" text-anchor="middle">
      🔒 Procesado de forma 100% segura por Mercado Pago
    </text>
  </g>
"""
cards[7] = get_base_svg("Todo tu año ordenado por $9.900", "oferta", card7_content, 7)

# Write SVGs and Convert to PNG
for num, svg_code in cards.items():
    svg_path = f"{OUTPUT_DIR}/card_{num}.svg"
    png_path = f"{OUTPUT_DIR}/card_{num}.png"
    
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_code)
    
    cmd = ["rsvg-convert", "-w", "1080", "-h", "1080", "-f", "png", "-o", png_path, svg_path]
    subprocess.run(cmd, check=True)
    print(f"Generated {png_path}")

print("All 7 cards generated successfully!")
