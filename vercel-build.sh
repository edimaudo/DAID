#!/bin/bash

# Stop immediately if any command fails
set -e

echo "--- STARTING BUILD ---"

# 1. Ensure the public folder exists
mkdir -p public

# 2. Smart Copy: Find the source file and create public/index.html
# If app.html is in the root, copy it to public/index.html
if [ -f "app.html" ]; then
    cp app.html public/index.html
    echo "✅ Copied root app.html to public/index.html"

# If app.html is ALREADY in public, duplicate it as index.html (if index.html doesn't exist)
elif [ -f "public/app.html" ] && [ ! -f "public/index.html" ]; then
    cp public/app.html public/index.html
    echo "✅ Copied public/app.html to public/index.html"
fi

# 3. Inject API Key into the final index.html
# This ensures the file served to users (index.html) has the key
if [ -f "public/index.html" ]; then
    sed -i "s|const apiKey = \"\";|const apiKey = \"$GEMINI_API_KEY\";|g" public/index.html
    echo "✅ Injected API Key into public/index.html"
else
    echo "❌ ERROR: public/index.html was not found. Build failed."
    exit 1
fi

echo "--- BUILD COMPLETE ---"
