#!/bin/bash

# OctoFit Tracker API Test Script
# Make sure the Django server is running before executing these commands

# Get the CODESPACE_NAME environment variable
CODESPACE_NAME="${CODESPACE_NAME}"

# Determine the base URL
if [ -n "$CODESPACE_NAME" ]; then
    BASE_URL="https://${CODESPACE_NAME}-8000.app.github.dev"
    echo "Testing API on Codespace: $BASE_URL"
else
    BASE_URL="http://localhost:8000"
    echo "Testing API on localhost: $BASE_URL"
fi

echo ""
echo "===================="
echo "Testing API Root"
echo "===================="
curl -X GET "${BASE_URL}/" -H "Accept: application/json"

echo ""
echo ""
echo "===================="
echo "Testing Users API"
echo "===================="
curl -X GET "${BASE_URL}/api/users/" -H "Accept: application/json"

echo ""
echo ""
echo "===================="
echo "Testing Teams API"
echo "===================="
curl -X GET "${BASE_URL}/api/teams/" -H "Accept: application/json"

echo ""
echo ""
echo "===================="
echo "Testing Activities API"
echo "===================="
curl -X GET "${BASE_URL}/api/activities/" -H "Accept: application/json"

echo ""
echo ""
echo "===================="
echo "Testing Workouts API"
echo "===================="
curl -X GET "${BASE_URL}/api/workouts/" -H "Accept: application/json"

echo ""
echo ""
echo "===================="
echo "Testing Leaderboard API"
echo "===================="
curl -X GET "${BASE_URL}/api/leaderboard/" -H "Accept: application/json"

echo ""
echo ""
echo "===================="
echo "All tests completed!"
echo "===================="
