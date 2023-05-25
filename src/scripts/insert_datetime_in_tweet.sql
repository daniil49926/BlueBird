CREATE OR REPLACE FUNCTION public.insert_datetime_in_tweet()
	RETURNS trigger AS
	$BODY$
	BEGIN
		if new._datetime is null then
			new._datetime := current_timestamp;
		end if;
		RETURN new;
	END;
	$BODY$
	LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER BI0_Tweet
	BEFORE INSERT ON public."Tweet"
	FOR EACH ROW EXECUTE FUNCTION insert_datetime_in_tweet();