-- PostgreSQL: kategooriad + tooted.kategooria_id nime järgi

CREATE TABLE kategooriad (
    kategooria_id   INTEGER        NOT NULL,
    nimetus         VARCHAR(50)    NOT NULL,
    osakond         VARCHAR(50)    NOT NULL,
    km_maar         NUMERIC(5, 2)  NOT NULL,
    PRIMARY KEY (kategooria_id),
    UNIQUE (nimetus)
);

INSERT INTO kategooriad (kategooria_id, nimetus, osakond, km_maar) VALUES
    (1, 'Arvutid',        'IT',            24),
    (2, 'Telefonid',      'Mobiil',        24),
    (3, 'Lisaseadmed',    'IT',            24),
    (4, 'Tahvelarvutid',  'Mobiil',        24),
    (5, 'Mängud',         'Meelelahutus',  22),
    (6, 'Mööbel',         'Kodu',          22);

ALTER TABLE tooted
    ADD COLUMN kategooria_id INTEGER;

UPDATE tooted t
SET kategooria_id = k.kategooria_id
FROM kategooriad k
WHERE t.kategooria = k.nimetus;

ALTER TABLE tooted
    ALTER COLUMN kategooria_id SET NOT NULL,
    ADD CONSTRAINT tooted_kategooria_fk
        FOREIGN KEY (kategooria_id) REFERENCES kategooriad (kategooria_id),
    DROP COLUMN kategooria;
