CREATE OR REPLACE PROCEDURE p_add_tweet(
	IN _content text, 
	IN _author int
)
	LANGUAGE plpgsql AS
$proc$
DECLARE _true_user int;
BEGIN
	select us.id from public."User" us
	INTO _true_user
	WHERE us.id = _author;
	if not found then
		raise notice'The user with id=% not found', _author;
	else
		insert into public."Tweet"(content, author)
			values(_content, _author);
		commit;
	end if;
END;
$proc$