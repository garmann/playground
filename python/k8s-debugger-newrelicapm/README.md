# README

this folder was used for k8s debugging. its running http requests from a container to desired target_url to generate apm data in new relic. we used it in k8s clusters to target other k8s clusters to run network debugging.

helm rendering might not work, stripped out some stuff, renamed files structure.

helm template --values ./values.yaml --output-dir ./rendered . --set "newrelic_license_key=foobar" --set "target_url="https://foobar" --set "sleep_seconds=5" --set "request_amount=100" -n foobar


docker run -d -e target_url="https://foobar" -e sleep_seconds=5 -e request_amount=5  -e NEW_RELIC_APP_NAME=foobar -e NEW_RELIC_LICENSE_KEY=foobar