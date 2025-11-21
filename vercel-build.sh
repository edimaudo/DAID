#!/bin/bash

# Stop immediately if any command fails
set -e

# 1. Create the standard output directory
mkdir -p public

# 2. Copy the source file (app.html) and rename it to the target (index.html)
# Vercel needs index.html to load the site automatically.
cp app.html public/index.html

# 3. Inject the Vercel Environment Variable using a temporary file (UNIVERSALLY COMPATIBLE)
INPUT_FILE="public/index.html"
TEMP_FILE="public/index.html.tmp"

# Execute sed: find the placeholder, replace it with the key, and write to a temporary file
sed "s|const apiKey = \"\";|const apiKey = \"$GEMINI_API_KEY\";|g" "$INPUT_FILE" > "$TEMP_FILE"

# Move the temporary file over the original file
mv "$TEMP_FILE" "$INPUT_FILE"

echo "Build successful. public/index.html created with API Key injected."
