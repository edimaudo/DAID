#!/bin/bash

# Stop immediately if any command fails
set -e

# 1. Create the standard output directory
mkdir -p public

# 2. Copy the source file (app.html) and rename it to the target (index.html)
# Vercel needs index.html to load the site automatically.
cp app.html public/index.html

# 3. Inject the Vercel Environment Variable into the final index.html
# Use the more compatible 'sed -i.bak' syntax to ensure in-place editing works on Linux/macOS environments.
sed -i.bak "s|const apiKey = \"\";|const apiKey = \"$GEMINI_API_KEY\";|g" public/index.html

# 4. Remove the temporary backup file created by sed (public/index.html.bak)
rm public/index.html.bak

echo "Build successful. public/index.html created with API Key injected."
