#!/bin/bash

set -e

INDEX_FILE="public/index.html"
APP_FILE="public/app.html"

# Function to perform safe key injection
safe_inject() {
    local FILE_PATH=$1
    local TEMP_FILE="${FILE_PATH}.tmp"

    if [ -f "$FILE_PATH" ]; then
        sed "s|const apiKey = \"\";|const apiKey = \"${GEMINI_API_KEY}\";|g" "$FILE_PATH" > "$TEMP_FILE"
        mv "$TEMP_FILE" "$FILE_PATH"
    fi
}

safe_inject "$INDEX_FILE"
safe_inject "$APP_FILE"
