#!/usr/bin/env bash
curl -i -H "Accept: application/json" -H "Content-Type: application/json" http://localhost:8080/todos/1
curl -X "DELETE" http://localhost:8080/todos/0
