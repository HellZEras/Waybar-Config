#!/bin/bash

# Get main audio volume level and mute status
main_volume=$(pamixer --get-volume-human)
main_icon=""  # Default icon for volume

# Check if main output is muted and adjust icon
if [[ "$main_volume" == "muted" ]]; then
    main_icon=""
fi

# Get microphone volume level
mic_volume=$(pamixer --default-source --get-volume-human)
mic_icon=""  # Icon for microphone

# Display combined volume and mic level
echo "$main_icon  $main_volume $mic_icon $mic_volume"
