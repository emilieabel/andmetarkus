# -*- coding: utf-8 -*-
"""Lihtne HTML-aruanne dim_organizations + fact_activities pealt."""

from __future__ import annotations

import os
from html import escape
from pathlib import Path

import psycopg2
import psycopg2.extras

KAUST = Path(__file__).resolve().parent
PAROOLIFAIL = KAUST / "parool.txt"
VALJUND = KAUST / "aruanne.html"


def loe_parool() -> str:
    if PAROOLIFAIL.is_file():
        rida = PAROOLIFAIL.read_text(encoding="utf-8").strip().splitlines()
        if rida and rida[0].strip():
            return rida[0].strip()
    kesk = os.environ.get("PGPASSWORD", "").strip()
    if kesk:
        return kesk
    raise SystemExit("Puudub parool.txt")


def tabel(headers, read) -> str:
    th = "".join(f"<th>{escape(str(h))}</th>" for h in headers)
    body = []
    for rida in read:
        td = "".join(f"<td>{escape('' if v is None else str(v))}</td>" for v in rida)
        body.append(f"<tr>{td}</tr>")
    return f"<table><tr>{th}</tr>{''.join(body)}</table>"


def main() -> None:
    conn = psycopg2.connect(
        host="localhost", port="5432", dbname="postgres",
        user="postgres", password=loe_parool(),
    )
    try:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM analytics.dim_organizations")
        org_n = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM analytics.fact_activities")
        act_n = cur.fetchone()[0]
        cur.execute(
            """
            SELECT status, COUNT(*) 
            FROM analytics.fact_activities
            GROUP BY status
            ORDER BY COUNT(*) DESC
            """
        )
        staatused = cur.fetchall()
        cur.execute(
            """
            SELECT
                COALESCE(d.parent_organization_name, '(ilma emaorganisatsioonita)') AS parent_organization_name,
                COUNT(DISTINCT d.organization_id) AS organization_count,
                COUNT(f.activity_id) AS activity_count
            FROM analytics.dim_organizations d
            LEFT JOIN analytics.fact_activities f
                ON f.lead_organization_id = d.organization_id
            GROUP BY 1
            ORDER BY activity_count DESC, organization_count DESC
            """
        )
        vanemad = cur.fetchall()
        cur.execute(
            """
            SELECT
                COALESCE(d.organization_name, '(tundmatu)') AS organization_name,
                d.organization_type,
                d.parent_organization_name,
                f.activity_name,
                f.status,
                f.progress_percent
            FROM analytics.fact_activities f
            LEFT JOIN analytics.dim_organizations d
                ON f.lead_organization_id = d.organization_id
            ORDER BY d.organization_name, f.activity_name
            """
        )
        read = cur.fetchall()
    finally:
        conn.close()

    html = f"""<!DOCTYPE html>
<html lang="et">
<head>
<meta charset="utf-8">
<title>Liikumisaktiivsus — aruanne</title>
<style>
  :root {{ --navy:#0f203e; --teal:#007073; --slate:#334155; --line:#d6dee8; }}
  body {{ margin:0 auto; max-width:1100px; padding:32px 40px 56px;
         font:16px/1.45 Calibri,"Segoe UI",sans-serif; color:var(--slate); }}
  h1 {{ color:var(--navy); margin:0 0 8px; }}
  .kicker {{ color:var(--teal); font-weight:700; font-size:13px; text-transform:uppercase; }}
  .kpi {{ display:flex; gap:16px; margin:20px 0 28px; }}
  .kpi div {{ flex:1; background:#f7f9fc; border-left:4px solid var(--teal); padding:14px 16px; }}
  .kpi b {{ display:block; font-size:28px; color:var(--navy); }}
  table {{ width:100%; border-collapse:collapse; margin:8px 0 28px; font-size:15px; }}
  th, td {{ border:1px solid var(--line); padding:6px 8px; text-align:left; vertical-align:top; }}
  th {{ background:var(--navy); color:white; }}
</style>
</head>
<body>
<p class="kicker">analytics.dim_organizations · analytics.fact_activities</p>
<h1>Liikumisaktiivsuse tegevused</h1>
<p>Allikas: liigume.ee API (organizations, activities). Emaorganisatsioon: parent_organization_id → parent_organization_name.</p>
<div class="kpi">
  <div>Organisatsioone<b>{org_n}</b></div>
  <div>Tegevusi<b>{act_n}</b></div>
</div>
<h2>Staatus</h2>
{tabel(["status", "activity_count"], staatused)}
<h2>Emaorganisatsioon</h2>
{tabel(["parent_organization_name", "organization_count", "activity_count"], vanemad)}
<h2>Tegevused juhtiva organisatsiooni kaupa</h2>
{tabel(["organization_name", "organization_type", "parent_organization_name", "activity_name", "status", "progress_percent"], read)}
</body>
</html>
"""
    VALJUND.write_text(html, encoding="utf-8")
    print(f"Aruanne: {VALJUND}")


if __name__ == "__main__":
    main()
