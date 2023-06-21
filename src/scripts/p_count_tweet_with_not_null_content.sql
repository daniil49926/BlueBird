CREATE OR REPLACE PROCEDURE p_count_tweet_with_not_null_content(
	INOUT _val int DEFAULT 0
)
	LANGUAGE plpgsql AS
$proc$
DECLARE 
	_curs CURSOR FOR SELECT * FROM public."Tweet";
    _row  RECORD;
BEGIN
	open _curs;
  	LOOP
   		FETCH FROM _curs INTO _row;
    	EXIT WHEN NOT FOUND;
		if _row.content is not null then
			_val := _val + 1;
		end if;
  END LOOP;
END;
$proc$