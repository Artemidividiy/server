-- Table: public.schemas

DROP TABLE IF EXISTS public.schemas;

CREATE TABLE IF NOT EXISTS public.schemas
(
    id bigint NOT NULL generated as identity,
    created_at timestamp without time zone,
    algo bigint,
    CONSTRAINT schemas_pkey PRIMARY KEY (id),
    CONSTRAINT algo FOREIGN KEY (algo)
        REFERENCES public.algotithms (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.schemas
    OWNER to postgres;


-- Table: public.algotithms

-- DROP TABLE IF EXISTS public.algotithms;

CREATE TABLE IF NOT EXISTS public.algotithms
(
    id bigint NOT NULL generated always as identity,
    name character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT algotithms_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.algotithms
    OWNER to postgres;

COMMENT ON TABLE public.algotithms
    IS 'contains list of algos';


-- Table: public.colors

-- DROP TABLE IF EXISTS public.colors;

CREATE TABLE IF NOT EXISTS public.colors
(
    id bigint NOT NULL generated as identity,
    name character varying COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp without time zone,
    hex character varying COLLATE pg_catalog."default" NOT NULL,
    rgb numeric[] NOT NULL,
    CONSTRAINT "Colors_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.colors
    OWNER to postgres;

COMMENT ON TABLE public.colors
    IS 'table contains only color info';


-- Table: public.colors_in_schemas

-- DROP TABLE IF EXISTS public.colors_in_schemas;

CREATE TABLE IF NOT EXISTS public.colors_in_schemas
(
    id bigint NOT NULL generated as identity,
    color bigint NOT NULL,
    schema bigint,
    CONSTRAINT colors_in_schemas_pkey PRIMARY KEY (id),
    CONSTRAINT color FOREIGN KEY (color)
        REFERENCES public.colors (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT schema FOREIGN KEY (schema)
        REFERENCES public.schemas (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.colors_in_schemas
    OWNER to postgres;


-- Table: public.liked_schemas

-- DROP TABLE IF EXISTS public.liked_schemas;

CREATE TABLE IF NOT EXISTS public.liked_schemas
(
    id bigint NOT NULL generated as identity,
    "user" bigint NOT NULL,
    scheme bigint,
    like_time timestamp without time zone,
    CONSTRAINT liked_schemas_pkey PRIMARY KEY (id),
    CONSTRAINT schemas_liked FOREIGN KEY (scheme)
        REFERENCES public.schemas (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT user_liked FOREIGN KEY ("user")
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.liked_schemas
    OWNER to postgres;

-- Trigger: add_created_at

DROP TRIGGER IF EXISTS add_created_at ON public.liked_schemas;

CREATE TRIGGER add_created_at
    AFTER INSERT
    ON public.liked_schemas
    FOR EACH ROW
    EXECUTE FUNCTION public.add_created_at_to_liked_schemas();


-- Table: public.users

-- DROP TABLE IF EXISTS public.users;

CREATE TABLE IF NOT EXISTS public.users
(
    id integer NOT NULL generated as identity,
    username character varying COLLATE pg_catalog."default" NOT NULL,
    password character varying COLLATE pg_catalog."default" NOT NULL,
    email character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "User_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to postgres;