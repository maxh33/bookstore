#!/bin/bash
# Backup diario do Postgres do bookstore (retencao 14 dias). Cron: 30 3 * * * ~/bookstore/backup.sh >> ~/bookstore/backups/backup.log 2>&1
set -euo pipefail
umask 077
BACKUP_DIR=~/bookstore/backups
mkdir -p "$BACKUP_DIR"
docker compose -f ~/bookstore/docker-compose.yml exec -T db sh -c 'pg_dump -U "$POSTGRES_USER" "$POSTGRES_DB"' \
  | gzip > "$BACKUP_DIR/bookstore-$(date +%F).sql.gz"
find "$BACKUP_DIR" -name 'bookstore-*.sql.gz' -mtime +14 -delete
