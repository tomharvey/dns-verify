# DNS Verify

A function to check DNS resolution and verify the correct setup of CNAMEs.

You can provide an FQDN and a list of acceptable CNAMEs, the function will
return with a list of CNAMEs which the FQDN resolves to and a boolean if any of
those are in the acceptable CNAMEs list.


## Installation

### Dependancies

Requires [serverless framework](http://serverless.com) and the
[serverless-python-requirements plugin]
(https://www.npmjs.com/package/serverless-python-requirements)

It also uses docker when deploying from a non-linux machine, to install the pip
requirements in a linux environment.


### Deployment

Then, the function can be deployed using `sls deploy --stage production` and it
will deploy to 'eu-west-1' by default, use the `--region REGION_ID` flag to
deploy elsewhere.


### Usage

Once deployed `sls` will report back with an API KEY and an HTTPS endpoint. We
will need to use these to make requests of the new service:


``` bash
curl -X POST \
  https://$API-ENDPOINT/production/validate-cname \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: $API_KEY' \
  -d '{
    "fqdn": "www.example.com",
    "valid-domains": "[example.com., non-valid.com.]"
}'
```

##### Example result
The result will come back as JSON:

``` json

{
    "success": {
        "valid": true,
        "cnames": [
            "example.com."
        ]
    }
}

```
