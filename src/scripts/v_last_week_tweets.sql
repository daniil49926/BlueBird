CREATE OR REPLACE VIEW v_last_week_tweets AS

	SELECT 
		tw.id,
		tw.content,
		tw.author,
		tw._datetime,
		count(tl.user_id),
		(
			select 
				count(tmr.id) as counts_media 
			from public."TweetMediaReferences" tmr
			where tmr.tweet_id = tw.id
		)

	FROM public."Tweet" tw
	LEFT JOIN public."TweetLikes" tl on tl.tweet_id = tw.id
	where tw._datetime > current_timestamp - interval '7 days'
	GROUP BY tw.id
	ORDER BY count(tl.user_id) DESC, tw._datetime;
	
ALTER VIEW v_last_week_tweets 
		RENAME COLUMN "count" TO "likes_count";