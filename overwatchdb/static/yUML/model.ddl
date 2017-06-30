DROP TABLE player_achievement CASCADE;

DROP TABLE player_reward CASCADE;

DROP TABLE achievement CASCADE;

DROP TABLE hero CASCADE;

DROP TABLE player CASCADE;

DROP TABLE reward CASCADE;

CREATE TABLE achievement (
id            INTEGER NOT NULL,
name          text NOT NULL,
description   text NOT NULL,
level          text NOT NULL,
hero_id       INTEGER,
reward_id     INTEGER
);

CREATE UNIQUE INDEX achievement__idx ON
achievement ( reward_id ASC );

ALTER TABLE achievement ADD CONSTRAINT achievement_pk PRIMARY KEY ( id );

CREATE TABLE hero (
id            INTEGER NOT NULL,
name          text NOT NULL,
description   text NOT NULL,
affiliation   text NOT NULL,
age           text NOT NULL
);

ALTER TABLE hero ADD CONSTRAINT hero_pk PRIMARY KEY ( id );

CREATE TABLE player (
id        INTEGER NOT NULL,
name      text NOT NULL,
server    text NOT NULL,
"level"   text NOT NULL,
hero_id   INTEGER
);

ALTER TABLE player ADD CONSTRAINT player_pk PRIMARY KEY ( id );

CREATE TABLE player_achievement (
player_id        INTEGER NOT NULL,
achievement_id   INTEGER NOT NULL
);

ALTER TABLE player_achievement ADD CONSTRAINT player_achievement_pk PRIMARY KEY ( player_id,achievement_id );

CREATE TABLE player_reward (
player_id   INTEGER NOT NULL,
reward_id   INTEGER NOT NULL
);

ALTER TABLE player_reward ADD CONSTRAINT player_reward_pk PRIMARY KEY ( player_id,reward_id );

CREATE TABLE reward (
id               INTEGER NOT NULL,
name             text NOT NULL,
quality          text NOT NULL,
cost             text NOT NULL,
hero_id          INTEGER,
achievement_id   INTEGER
);

CREATE UNIQUE INDEX reward__idx ON
reward ( achievement_id ASC );

ALTER TABLE reward ADD CONSTRAINT reward_pk PRIMARY KEY ( id );

ALTER TABLE achievement ADD CONSTRAINT achievement_hero_fk FOREIGN KEY ( hero_id )
REFERENCES hero ( id );

ALTER TABLE achievement ADD CONSTRAINT achievement_reward_fk FOREIGN KEY ( reward_id )
REFERENCES reward ( id );

ALTER TABLE player_achievement ADD CONSTRAINT player_achievement_achievement_fk FOREIGN KEY ( achievement_id )
REFERENCES achievement ( id );

ALTER TABLE player_achievement ADD CONSTRAINT player_achievement_player_fk FOREIGN KEY ( player_id )
REFERENCES player ( id );

ALTER TABLE player ADD CONSTRAINT player_hero_fk FOREIGN KEY ( hero_id )
REFERENCES hero ( id );

ALTER TABLE player_reward ADD CONSTRAINT player_reward_player_fk FOREIGN KEY ( player_id )
REFERENCES player ( id );

ALTER TABLE player_reward ADD CONSTRAINT player_reward_reward_fk FOREIGN KEY ( reward_id )
REFERENCES reward ( id );

ALTER TABLE reward ADD CONSTRAINT reward_achievement_fk FOREIGN KEY ( achievement_id )
REFERENCES achievement ( id );

ALTER TABLE reward ADD CONSTRAINT reward_hero_fk FOREIGN KEY ( hero_id )
REFERENCES hero ( id );

commit;
