import os

import requests
from six.moves.urllib.parse import urljoin, quote


BIPORTAL = "http://data.bioontology.org"


def get_snomed_term_for_mesh_term(self, mesh_term):
    """
    Use the
    :param mesh_term:
    :return:
    """
    session = requests.Session()
    session.headers.update({'Authorization': 'apikey token={}'.format(os.getenv('BIOPORTALKEY'))})
    mesh_term = "/search?q={}&ontologies=MESH&require_exact_match=true".format(quote(mesh_term))
    response = session.get(urljoin(BIPORTAL, mesh_term))
    if response.status_code == 200:
        result = response.json()
        if result.get('totalCount') == 0:
            print("Term not found")
            return {}
        print("Got {}".format(result.get('totalCount')))
        itm = result.get('collection')[0]
        mappings = session.get(itm.get('links').get('mappings'))
        if mappings.status_code == 200:
            _m = mappings.json()
            print("Got {} total mappings".format(len(_m)))
            for mm in _m:
                to_class = mm.get('classes')[1]
                if to_class.get('links', {}).get('ontology',
                                                 '') == "http://data.bioontology.org/ontologies/SNOMEDCT":
                    # retrieve the snomed term
                    snomed_q = session.get(to_class.get('links', {}).get('self', ''))
                    if snomed_q.status_code == 200:
                        snomed = snomed_q.json()
                        # hacky
                        snomed_term = snomed.get("@id").split('/')[-1]
                        return snomed_term
    return {}
