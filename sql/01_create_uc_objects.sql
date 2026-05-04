CREATE CATALOG IF NOT EXISTS PRJ__vattenfall_01;

CREATE SCHEMA IF NOT EXISTS PRJ__vattenfall_01.raw;
CREATE SCHEMA IF NOT EXISTS PRJ__vattenfall_01.refined;
CREATE SCHEMA IF NOT EXISTS PRJ__vattenfall_01.analytics;

CREATE VOLUME IF NOT EXISTS PRJ__vattenfall_01.raw.landing;
CREATE VOLUME IF NOT EXISTS PRJ__vattenfall_01.raw.checkpoints;
