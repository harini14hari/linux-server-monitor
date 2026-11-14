
#!/bin/bash

# Project directory
SOURCE_DIR="$HOME/linux-server-monitor"

# Backup directory
BACKUP_DIR="$SOURCE_DIR/backups"

# Generate timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Backup filename
BACKUP_FILE="$BACKUP_DIR/linux-server-monitor_$TIMESTAMP.tar.gz"

echo "=================================================="
echo "          LINUX SERVER BACKUP"
echo "=================================================="

# Create compressed backup
tar -czf "$BACKUP_FILE" \
    --exclude="backups" \
    -C "$(dirname "$SOURCE_DIR")" \
    "$(basename "$SOURCE_DIR")"

# Check backup result
if [ $? -eq 0 ]; then
    echo "Backup completed successfully!"
    echo "Backup file: $BACKUP_FILE"
else
    echo "ERROR: Backup failed!"
fi

echo "=================================================="
