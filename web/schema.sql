CREATE TABLE IF NOT EXISTS events (
                                    id integer PRIMARY KEY ASC AUTOINCREMENT,
                                    date text NOT NULL,
                                    authenticated integer NOT NULL
                                );      
CREATE TABLE IF NOT EXISTS users (
                                    id integer PRIMARY KEY ASC AUTOINCREMENT,
                                    name text NOT NULL,
                                    password text NOT NULL,
                                    email text NOT NULL,
                                    isadmin integer NOT NULL
                                );
