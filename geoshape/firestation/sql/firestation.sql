--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

--
-- Name: firestations; Type: VIEW; Schema: public; Owner: -
--

CREATE VIEW firestations AS
 SELECT c.id,
    c.objectid,
    c.permanent_identifier,
    c.source_featureid,
    c.source_datasetid,
    c.source_datadesc,
    c.source_originator,
    c.data_security,
    c.distribution_policy,
    c.loaddate,
    c.ftype,
    c.fcode,
    c.name,
    c.islandmark,
    c.pointlocationtype,
    c.admintype,
    c.addressbuildingname,
    c.address,
    c.city,
    c.state,
    c.zipcode,
    c.gnis_id,
    c.foot_id,
    c.complex_id,
    c.globalid,
    c.geom,
    sum(d.firefighter) AS "Total Firefighters",
    sum(d.firefighter_emt) AS "Total Firefighter/EMTS",
    sum(d.firefighter_paramedic) AS "Total Firefighter/Paramedics",
    sum(d.ems_emt) AS "Total EMS only EMTs",
    sum(d.ems_paramedic) AS "Total EMS only Paramedics",
    sum(d.officer) AS "Total Officers",
    sum(d.officer_paramedic) AS "Total Officer/Paramedics",
    sum(d.ems_supervisor) AS "Total EMS Supervisors",
    sum(d.chief_officer) AS "Total Chief Officers"
   FROM (((firestation_firecaresbase a
     JOIN firestation_firestation b ON ((a.id = b.firecaresbase_ptr_id)))
     JOIN firestation_usgsstructuredata c ON ((b.usgsstructuredata_ptr_id = c.id)))
     JOIN firestation_responsecapability d ON ((c.id = d.firestation_id)))
  GROUP BY c.id;


--
-- PostgreSQL database dump complete
--

