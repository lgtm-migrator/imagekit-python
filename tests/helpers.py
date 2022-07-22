import base64
import unittest
from unittest.mock import Mock, patch

from requests import Response

from imagekitio.client import ImageKit
from tests.dummy_data.file import AUTHENTICATION_ERR_MSG, SUCCESS_GENERIC_RESP

try:
    from simplejson.errors import JSONDecodeError
except ImportError:
    from json import JSONDecodeError


class ClientTestCase(unittest.TestCase):
    """
    Base TestCase for Client
    """
    private_key = "fake122"

    @patch("imagekitio.file.File")
    @patch("imagekitio.resource.ImageKitRequest")
    def setUp(self, mock_file, mock_req):
        """
        Tests if list_files work with skip and limit
        """
        self.options = {
            "type": "file",
            "sort": "ASC_CREATED",
            "path": "/",
            "searchQuery": "createdAt >= '2d' OR size < '2mb' OR format='png'",
            "fileType": "all",
            "limit": 1,
            "skip": 0,
            "tags": "Tag-1, Tag-2, Tag-3"
        }
        self.client = ImageKit(
            public_key="fake122", private_key=ClientTestCase.private_key, url_endpoint="fake122",
        )


def get_mocked_failed_resp(message=None, status=401):
    """GET failed mocked response customized by parameter
    """
    mocked_resp = Mock(spec=Response)
    mocked_resp.status_code = status
    mocked_resp.headers = "headers"
    if not message:
        mocked_resp.json.return_value = AUTHENTICATION_ERR_MSG
    else:
        mocked_resp.json.return_value = message
    return mocked_resp


def get_mocked_failed_resp_text():
    """GET failed mocked response returned as text not json
    """
    mocked_resp = Mock(spec=Response)
    mocked_resp.status_code = 502
    mocked_resp.text = 'Bad Gateway'
    mocked_resp.headers = 'headers'
    mocked_resp.json.side_effect = JSONDecodeError("Expecting value: ", "Bad Gateway", 0)
    return mocked_resp


def get_mocked_success_resp(message: dict = None, status: int = 200, resp: dict = None):
    """GET success mocked response customize by parameter
    """
    mocked_resp = Mock(spec=Response)
    mocked_resp.status_code = status
    mocked_resp.headers = "headers"
    if message and resp:
        response = {}
        response.update(message)
        response.update(resp)
        mocked_resp.json.return_value = response
    elif message:
        mocked_resp.json.return_value = message
    elif resp:
        mocked_resp.json.return_value = resp
    else:
        mocked_resp.json.return_value = SUCCESS_GENERIC_RESP
    return mocked_resp


def create_headers_for_test():
    headers = {"Accept-Encoding": "gzip, deflate"}
    headers.update(get_auth_headers_for_test())
    return headers


def get_auth_headers_for_test():
    encoded_private_key = base64.b64encode((ClientTestCase.private_key + ":").encode()).decode(
        "utf-8"
    )
    return {"Authorization": "Basic {}".format(encoded_private_key)}
