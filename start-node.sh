#!/bin/bash
sudo mkdir -p /var/lib/tailscale
pgrep tailscaled > /dev/null || sudo tailscaled --state=/var/lib/tailscale/tailscaled.state > /tmp/ts.log 2>&1 &
sleep 5
sudo tailscale up --hostname=cloud0
sudo service ssh start
tailscale ip -4