-- Table: public.room

-- DROP TABLE IF EXISTS public.room;

CREATE TABLE IF NOT EXISTS public.room
(
    "RoomID" bigint NOT NULL,
    "RoomType" character varying(10) COLLATE pg_catalog."default" NOT NULL,
    "Available" character varying(5) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT room_pkey PRIMARY KEY ("RoomID")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.room
    OWNER to postgres;