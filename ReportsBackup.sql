PGDMP     4    "                z           Reports    14.3    14.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16394    Reports    DATABASE     m   CREATE DATABASE "Reports" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE "Reports";
                postgres    false            �            1259    16396    running_reports    TABLE     !  CREATE TABLE public.running_reports (
    id integer NOT NULL,
    fname character varying(100) NOT NULL,
    lname character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    report_name character varying(100),
    start_time timestamp with time zone DEFAULT now()
);
 #   DROP TABLE public.running_reports;
       public         heap    postgres    false            �            1259    16395    running_reports_id_seq    SEQUENCE     �   CREATE SEQUENCE public.running_reports_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.running_reports_id_seq;
       public          postgres    false    210            �           0    0    running_reports_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.running_reports_id_seq OWNED BY public.running_reports.id;
          public          postgres    false    209            \           2604    16399    running_reports id    DEFAULT     x   ALTER TABLE ONLY public.running_reports ALTER COLUMN id SET DEFAULT nextval('public.running_reports_id_seq'::regclass);
 A   ALTER TABLE public.running_reports ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    210    209    210            �          0    16396    running_reports 
   TABLE DATA           [   COPY public.running_reports (id, fname, lname, email, report_name, start_time) FROM stdin;
    public          postgres    false    210   1       �           0    0    running_reports_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.running_reports_id_seq', 1, true);
          public          postgres    false    209            _           2606    16404 )   running_reports running_reports_email_key 
   CONSTRAINT     e   ALTER TABLE ONLY public.running_reports
    ADD CONSTRAINT running_reports_email_key UNIQUE (email);
 S   ALTER TABLE ONLY public.running_reports DROP CONSTRAINT running_reports_email_key;
       public            postgres    false    210            a           2606    16402 $   running_reports running_reports_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.running_reports
    ADD CONSTRAINT running_reports_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.running_reports DROP CONSTRAINT running_reports_pkey;
       public            postgres    false    210            �   `   x�3������,����-(���,(��R�3��S��2�S���RK8=CB\�C<��9���tLu������L���M��t̹b���� �}?     