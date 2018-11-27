"""Resolve DNS names."""
from dns import resolver


def valid_cname(fqdn, valid_domains):
    """Check that the host resolves to a CNAME in the valid_domains list."""
    try:
        answers = resolver.query(fqdn, 'CNAME')
    except resolver.NoAnswer:
        return False, []

    cnames = [_answer_to_text(answer) for answer in answers]
    for cname in cnames:
        if cname in valid_domains:
            return True, cnames
    return False, cnames


def _answer_to_text(answer):
    """Convert the dns.resolver.Answer to text."""
    return answer.to_text()
