import requests
from six.moves.urllib.parse import urljoin

RXNORMAPI = "https://rxnav.nlm.nih.gov/REST/"


def get_rxnorm_code_from_name(med_name):
    """
    Get a RxNORM code
    :param med_name:
    :return:
    """
    session = requests.Session()
    got = session.get(urljoin(RXNORMAPI, "rxcui.json?name={}".format(quote(med_name))))
    if got.status_code == 200:
        return got.json()
    return {}

