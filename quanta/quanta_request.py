import quanta_client
from quanta_client.rest import ApiException

# create an instance of the API class
api_client = quanta_client.ApiClient(host='https://quanta.infra.cloudera.com:8443/api/v1/',
                                     header_name='content-type',
                                     header_value='application/json', cookie=None)
tr_api_instance = quanta_client.TestReportsApi(api_client)


def get_gtn_current_state(gtn):
    try:
        api_response = tr_api_instance.get_test_report(gtn)
        return api_response.state
    except ApiException as e:
        print("Exception: %s\n" % e)
