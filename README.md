# Redwall

A system for notetaking in Markdown.

## How to use

Look up how to use Poetry if you want more functionality

```
poetry run gunicorn redwall:app
```

## Introduction

Goals: should be as simple as possible and as few dependencies as possible. 

Components:
1. Web Server: business logic to call the correct endpoints
2. Storage (Sqlite interface)
3. Markdown Parser (Pandoc interface)
4. HTML templates (Jinja2)


Inspired by Anno note taking tool: https://github.com/gwgundersen/anno
