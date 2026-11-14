
#!/bin/bash

echo "=================================================="
echo "          LINUX SERVER HEALTH CHECK"
echo "=================================================="

# 1. Check hostname
echo ""
echo "Hostname:"
hostname

# 2. Check CPU load
echo ""
echo "CPU Load:"
uptime

# 3. Check memory usage
echo ""
echo "Memory Usage:"
free -h

# 4. Check disk usage
echo ""
echo "Disk Usage:"
df -h /

# 5. Check system uptime
echo ""
echo "System Uptime:"
uptime -p

echo ""
echo "=================================================="
echo "          HEALTH CHECK COMPLETED"
echo "=================================================="
