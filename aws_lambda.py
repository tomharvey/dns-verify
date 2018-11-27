"""Interface for AWS Lambda endpoints.

Handles HTTP request parameter parsing and creation of responses.
"""
import json
from dns_verify import valid_cname


def validate_cname(event, context):
    """Handle the Lambda call and check the CNAME validity."""
    data = json.loads(event['body'])

    try:
        fqdn = data['fqdn']
        valid_domains = data['valid-domains']
    except KeyError:
        return KEY_ERROR_RESULT

    is_valid, cnames = valid_cname(fqdn, valid_domains)
    body = json.dumps({
        'success': {
            'is-valid': is_valid,
            'cnames': cnames,
        }
    })

    return {
        "statusCode": 200,
        "body": body,
    }


KEY_ERROR_RESULT = {
    "statusCode": 400,
    "body": json.dumps({
        'error': {
            'message': 'must post `fqdn` and `valid-domains` params'
        }
    }),
}
