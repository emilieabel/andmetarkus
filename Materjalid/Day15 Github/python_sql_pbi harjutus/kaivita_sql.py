# -*- coding: utf-8 -*-
"""Käivitab loo_tahtskeem.sql: loob protseduuri ja kutsub selle."""

from __future__ import annotations

import os
from pathlib import Path

import psycopg2

KAUST = Path(__file__).resolve().parent
PAROOLIFAIL = KAUST / "parool.txt"
SQL_FAIL = KAUST / "loo_tahtskeem.sql"


def loe_parool() -> str:
    if PAROOLIFAIL.is_file():
        rida = PAROOLIFAIL.read_text(encoding="utf-8").strip().splitlines()
        if rida and rida[0].strip():
            return rida[0].strip()
    kesk = os.environ.get("PGPASSWORD", "").strip()
    if kesk:
        return kesk
    raise SystemExit("Puudub parool.txt")


def main() -> None:
    sql = SQL_FAIL.read_text(encoding="utf-8")
    algus = sql.find("CREATE OR REPLACE PROCEDURE")
    lopp = sql.rfind("$$;") + 3
    protseduur = sql[algus:lopp]

    conn = psycopg2.connect(
        host="localhost", port="5432", dbname="postgres",
        user="postgres", password=loe_parool(),
    )
    try:
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute("CREATE SCHEMA IF NOT EXISTS analytics")
            cur.execute(protseduur)
            cur.execute("CALL analytics.refresh_organization_activity_star()")
        print("SQL-protseduur käivitatud: analytics.dim_organizations, analytics.fact_activities.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
