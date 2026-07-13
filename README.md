# Dashboard Piramide Home

Dashboard de performance de Piramide Home (Krab-e). `index.html` self-contained que lee **en vivo** de Supabase (proyecto `krab-e-dashboards`) con la anon key publishable (solo lectura, RLS `anon_read`).

## Fuentes de datos

Tablas Supabase pobladas por 4 workflows n8n (carga diaria 08:00) desde el Sheet de Detrics del cliente:

- `piramidehome_meta_ads` — Meta Ads (pestana `meta`)
- `piramidehome_google_ads` — Google Ads (pestana `google`)
- `piramidehome_ga4_sessions` — GA4 (pestana `analytics`)
- `piramidehome_tiendanube_orders` — Facturacion (pestana `facturacion_manual`)

## Metricas

Enfoque ACOS / performance: inversion total (Meta + Google), facturacion (ordenes pagas), ACOS, ROAS, CTR/CPC/CPM por plataforma, sesiones y transacciones GA4, y ticket promedio.

## UI

Branding Krab-e (fondo `#191919`, naranja `#ff700a`, General Sans + Bitroad en titulos, Satoshi en numeros, grain overlay). Selector de fecha tipo Looker con presets (Mes actual / 7d / 30d / 90d / Todo) + rango Desde/Hasta; default = mes en curso.

## Build

```bash
python3 build_dashboard.py   # inyecta assets de branding y genera index.html
```
