# -*- coding: utf-8 -*-
"""Bronze: organizations + activities API → schema bronze_liikumisaktiivsuse_api.

Kõik veerud. Tabelid kirjutatakse iga kord üle. Dim/fact tuleb SQL-protseduurist.
Käivitus: kaivita_harjutus.bat
"""

from __future__ import annotations

import json
import os
import urllib.request
from datetime import date
from pathlib import Path

import psycopg2
from psycopg2.extras import execute_values

KAUST = Path(__file__).resolve().parent
PAROOLIFAIL = KAUST / "parool.txt"
SKEEM = "bronze_liikumisaktiivsuse_api"

URL_ORGANIZATIONS = "https://app.liigume.ee/api/organizations"
URL_ACTIVITIES = "https://app.liigume.ee/api/activities"


def loe_parool() -> str:
    if PAROOLIFAIL.is_file():
        rida = PAROOLIFAIL.read_text(encoding="utf-8").strip().splitlines()
        if rida and rida[0].strip():
            return rida[0].strip()
    kesk = os.environ.get("PGPASSWORD", "").strip()
    if kesk:
        return kesk
    raise SystemExit("Puudub parool.txt")


def tyhi(vaartus):
    if vaartus is None:
        return None
    tekst = str(vaartus).strip()
    return tekst if tekst else None


def taisarv(vaartus):
    if vaartus is None or vaartus == "":
        return None
    return int(vaartus)


def kuupaev(vaartus):
    tekst = tyhi(vaartus)
    if not tekst:
        return None
    try:
        return date.fromisoformat(tekst[:10])
    except ValueError:
        return None


def json_tekst(vaartus):
    if vaartus is None:
        return None
    return json.dumps(vaartus, ensure_ascii=False, sort_keys=True)


def lae_json(url: str) -> list:
    print(f"Laen: {url}")
    paring = urllib.request.Request(
        url,
        headers={"User-Agent": "Andmetarkus-harjutus/1.0", "Accept": "application/json"},
    )
    with urllib.request.urlopen(paring, timeout=120) as vastus:
        andmed = json.loads(vastus.read().decode("utf-8"))
    if not isinstance(andmed, list):
        raise SystemExit(f"Ootasin nimekirja: {url}")
    print(f"  ridu: {len(andmed)}")
    return andmed


def main() -> None:
    organizations = lae_json(URL_ORGANIZATIONS)
    activities = lae_json(URL_ACTIVITIES)

    org_read = [
        (
            taisarv(r.get("id")),
            tyhi(r.get("name")) or "",
            tyhi(r.get("abbreviation")),
            tyhi(r.get("org_type")),
            taisarv(r.get("parent_organization_id")),
        )
        for r in organizations
    ]
    act_read = [
        (
            taisarv(r.get("id")),
            tyhi(r.get("name")) or "",
            taisarv(r.get("nr")),
            tyhi(r.get("code")),
            tyhi(r.get("name_short")),
            tyhi(r.get("activity_type")),
            tyhi(r.get("period")),
            kuupaev(r.get("start_date")),
            kuupaev(r.get("end_date")),
            tyhi(r.get("target_outcome")),
            tyhi(r.get("description")),
            json_tekst(r.get("target_groups")),
            tyhi(r.get("status")),
            taisarv(r.get("progress_pct")),
            taisarv(r.get("who_direction_id")),
            taisarv(r.get("lead_org_id")),
            tyhi(r.get("read_more_link")),
            tyhi(r.get("last_modified_time")),
            json_tekst(r.get("partner_ids")),
            json_tekst(r.get("policy_ids")),
            json_tekst(r.get("research_ids")),
            json_tekst(r.get("indicators")),
        )
        for r in activities
    ]

    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="postgres",
        user="postgres",
        password=loe_parool(),
    )
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(f"CREATE SCHEMA IF NOT EXISTS {SKEEM}")
                cur.execute(f"DROP TABLE IF EXISTS {SKEEM}.activities")
                cur.execute(f"DROP TABLE IF EXISTS {SKEEM}.organizations")
                cur.execute(
                    f"""
                    CREATE TABLE {SKEEM}.organizations (
                        organization_id INTEGER PRIMARY KEY,
                        organization_name VARCHAR(400) NOT NULL,
                        abbreviation VARCHAR(50),
                        organization_type VARCHAR(100),
                        parent_organization_id INTEGER
                    )
                    """
                )
                cur.execute(
                    f"""
                    CREATE TABLE {SKEEM}.activities (
                        activity_id INTEGER PRIMARY KEY,
                        activity_name VARCHAR(500) NOT NULL,
                        activity_number INTEGER,
                        activity_code VARCHAR(50),
                        short_name VARCHAR(400),
                        activity_type VARCHAR(200),
                        period VARCHAR(50),
                        start_date DATE,
                        end_date DATE,
                        target_outcome TEXT,
                        description TEXT,
                        target_groups TEXT,
                        status VARCHAR(100),
                        progress_percent INTEGER,
                        direction_id INTEGER,
                        lead_organization_id INTEGER,
                        read_more_link TEXT,
                        last_modified_time VARCHAR(50),
                        partner_identifiers TEXT,
                        policy_identifiers TEXT,
                        research_identifiers TEXT,
                        indicators TEXT
                    )
                    """
                )
                execute_values(
                    cur,
                    f"""
                    INSERT INTO {SKEEM}.organizations (
                        organization_id, organization_name, abbreviation,
                        organization_type, parent_organization_id
                    ) VALUES %s
                    """,
                    org_read,
                )
                execute_values(
                    cur,
                    f"""
                    INSERT INTO {SKEEM}.activities (
                        activity_id, activity_name, activity_number, activity_code,
                        short_name, activity_type, period, start_date, end_date,
                        target_outcome, description, target_groups, status,
                        progress_percent, direction_id, lead_organization_id,
                        read_more_link, last_modified_time, partner_identifiers,
                        policy_identifiers, research_identifiers, indicators
                    ) VALUES %s
                    """,
                    act_read,
                )
        print(f"Bronze üle kirjutatud: organizations {len(org_read)}, activities {len(act_read)}.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
