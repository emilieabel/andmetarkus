-- Dimensioon ja fakt. Käivitab protseduuri (ei ole Python).
-- parent_organization_name = emaorganisatsiooni nimi parent_organization_id järgi.

CREATE SCHEMA IF NOT EXISTS analytics;

CREATE OR REPLACE PROCEDURE analytics.refresh_organization_activity_star()
LANGUAGE plpgsql
AS $$
BEGIN
    DROP TABLE IF EXISTS analytics.fact_activities;
    DROP TABLE IF EXISTS analytics.dim_organizations;

    CREATE TABLE analytics.dim_organizations (
        organization_id INTEGER PRIMARY KEY,
        organization_name VARCHAR(400) NOT NULL,
        abbreviation VARCHAR(50),
        organization_type VARCHAR(100),
        parent_organization_id INTEGER,
        parent_organization_name VARCHAR(400)
    );

    INSERT INTO analytics.dim_organizations (
        organization_id,
        organization_name,
        abbreviation,
        organization_type,
        parent_organization_id,
        parent_organization_name
    )
    SELECT
        child.organization_id,
        child.organization_name,
        child.abbreviation,
        child.organization_type,
        child.parent_organization_id,
        parent.organization_name
    FROM bronze_liikumisaktiivsuse_api.organizations AS child
    LEFT JOIN bronze_liikumisaktiivsuse_api.organizations AS parent
        ON child.parent_organization_id = parent.organization_id;

    CREATE TABLE analytics.fact_activities (
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
    );

    INSERT INTO analytics.fact_activities
    SELECT
        activity_id,
        activity_name,
        activity_number,
        activity_code,
        short_name,
        activity_type,
        period,
        start_date,
        end_date,
        target_outcome,
        description,
        target_groups,
        status,
        progress_percent,
        direction_id,
        lead_organization_id,
        read_more_link,
        last_modified_time,
        partner_identifiers,
        policy_identifiers,
        research_identifiers,
        indicators
    FROM bronze_liikumisaktiivsuse_api.activities;

    COMMENT ON TABLE analytics.dim_organizations IS
        'Organisatsioonid. parent_organization_name tuleb parent_organization_id järgi samast bronze tabelist.';
    COMMENT ON COLUMN analytics.dim_organizations.parent_organization_name IS
        'Emaorganisatsiooni nimi (parent company), leitud parent_organization_id kaudu.';
    COMMENT ON TABLE analytics.fact_activities IS
        'Tegevused. lead_organization_id ühendub dim_organizations.organization_id-ga.';
END;
$$;

CALL analytics.refresh_organization_activity_star();
