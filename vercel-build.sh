#!/bin/bash

# Inject the Vercel Environment Variable into the files in the public folder
sed -i "s|const apiKey = \"\";|const apiKey = \"$GEMINI_API_KEY\";|g" public/index.html
sed -i "s|const apiKey = \"\";|const apiKey = \"$GEMINI_API_KEY\";|g" public/app.html
