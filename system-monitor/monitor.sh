#!/bin/bash

# ─── System Monitor Script ───────────────────────────
# Author: Dilukshi Warangana
# Description: Monitors CPU, Memory, and Disk usage
# ─────────────────────────────────────────────────────

THRESHOLD=80

echo "=============================="
echo "   System Monitor Report"
echo "   $(date)"
echo "=============================="

# ── CPU Usage ──
CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
echo "CPU Usage   : $CPU%"
if (( $(echo "$CPU > $THRESHOLD" | bc -l) )); then
    echo "⚠️  WARNING: CPU usage is high!"
fi
# ── Memory Usage ──
MEM=$(free | grep Mem | awk '{printf("%.1f"), $3/$2 * 100}')
echo "Memory Usage: $MEM%"
if (( $(echo "$MEM > $THRESHOLD" | bc -l) )); then
	echo "⚠️  WARNING: Memory usage is high!"
fi

# ── Disk Usage ──
DISK=$(df / | grep / | awk '{print $5}' | cut -d'%' -f1)
echo "Disk Usage  : $DISK%"
if (( $DISK > $THRESHOLD )); then
	echo "⚠️  WARNING: Disk usage is high!"
fi

echo "=============================="
echo "✅ Monitor check complete"
echo "=============================="
