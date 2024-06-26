INSERT INTO TV_SHOW_RECORDS VALUES (
    1
    ,1
    , 'The Office',
    2005
    , 1
    , 1
    , 120
    , 'tt0386676'
    , '<NAME>, <NAME>, <NAME>'
    , '<NAME>'
    , 'USA'
    , 'TV'
    , 'Comedy'
    , 'The misadventures of <NAME> and <NAME> in the world of high-stakes negotiations.'
);

PRAGMA table_info(TV_SHOW_RECORDS);
SELECT * FROM TV_SHOW_RECORDS LIMIT 10;
DELETE FROM TV_SHOW_RECORDS;
SELECT COUNT(*) FROM tv_show_records WHERE year IS NULL or year = '';
UPDATE tv_show_records SET year = 0 WHERE year IS NULL OR year = ''; 
