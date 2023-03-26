BEGIN;

CREATE TABLE mock_table 
(
    id SERIAL PRIMARY KEY,
    name CHARACTER VARYING(50)
);

INSERT INTO mock_table (name) VALUES ('cat'), ('dog'), ('whale');

COMMIT;