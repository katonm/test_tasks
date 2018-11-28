#!/bin/bash
psql -d test_db -U test_user -c "SELECT Name, COUNT(msg) FROM users JOIN messages ON users.UID = messages.UID group by name ;"