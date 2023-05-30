CREATE SEQUENCE IF NOT EXISTS public."TweetHist_id_seq"
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

CREATE TABLE IF NOT EXISTS public."TweetHist"
(
    id integer NOT NULL DEFAULT nextval('"TweetHist_id_seq"'::regclass),
    id_tweet integer NOT NULL,
	content character varying COLLATE pg_catalog."default" NOT NULL,
    author integer NOT NULL,
    _datetime_add timestamp without time zone,
	_datetime_del timestamp without time zone,
    CONSTRAINT "TweetHist_pkey" PRIMARY KEY (id),
    CONSTRAINT "TweetHist_author_fkey" FOREIGN KEY (author)
        REFERENCES public."User" (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)