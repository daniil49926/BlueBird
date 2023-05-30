CREATE OR REPLACE FUNCTION public.insert_tweets_hist()
	RETURNS trigger AS
	$BODY$
	BEGIN
		INSERT INTO public."TweetHist"(
			id_tweet, 
			content, 
			author, 
			_datetime_add, 
			_datetime_del
		)
		VALUES(
		old.id,
		old.content,
		old.author,
		old._datetime,
		current_timestamp
		);
		RETURN NULL;
	END;
	$BODY$
	LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER AD0_Tweet
	AFTER DELETE ON public."Tweet"
	FOR EACH ROW EXECUTE FUNCTION insert_tweets_hist();
