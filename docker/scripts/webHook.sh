#!/bin/bash
source GitHubToken

github_url="https://api.github.com/repos/marrinosnis/morse/hooks"

# Create Webhook URL in the GitHub with the below curl command
public_ngrok_url=$(curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE 's/.*public_url":"https:..([^"]*).*/\1/p')
curl -L \
     -X POST \
     -H "Accept: application/vnd.github+json" \
     -H "Authorization: Bearer $github_token" \
     -H "X-GitHub-Api-Version: 2022-11-28" \
     "$github_url" \
     -d "{\"name\":\"web\", \"active\":true, \"events\":[\"push\"],\"config\":{\"url\":\"https://$public_ngrok_url/github-webhook/\",\"content_type\":\"json\",\"insecure_ssl\":\"0\"}}"


#Retrieve the current Webhook, and store the id of it in order to perform a Delete post request.
#hook_id=$(curl -H "Authorization: token $github_token" "$github_url" | sed -n 's/.*"id": \([^,]*\).*/\1/p')
#
##Perfrom a delete post request to remove
#curl -L \
#     -X DELETE \
#     -H "Accept: application/vnd.github+json" \
#     -H "Authorization: Bearer $github_token" \
#     -H "X-GitHub-Api-Version: 2022-11-28" "$github_url/$hook_id"