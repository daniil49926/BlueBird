CREATE OR REPLACE PROCEDURE p_count_tweets(
	INOUT _val int DEFAULT null
)
	LANGUAGE plpgsql AS
$proc$
BEGIN
	select count(tw.id) from public."Tweet" tw
	INTO _val;
END;
$proc$