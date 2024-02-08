from unittest.mock import patch, Mock

import pytest
import requests

from twitter import Twitter


class ResponseGetMock(object):
    def json(self):
        return {'avatar_url': 'test'}


@pytest.fixture(params=[None, 'python'])
def username(request):
    return request.param


@pytest.fixture(params=['list', 'backend'], name='twitter')
def fixture_twitter(backend, username, request, monkeypatch):
    if request.param == 'list':
        twitter = Twitter(username=username)
    elif request.param == 'backend':
        twitter = Twitter(backend=backend, username=username)
    return twitter


def test_initizalization(twitter):
    assert twitter


@patch.object(requests, 'get', return_value=ResponseGetMock())
def test_tweet_single_message(avatar_mock, twitter):
    twitter.tweet('Test message')
    assert twitter.tweet_messages == ['Test message']


class MagicMock:
    pass


def test_tweet_long_message(twitter):
    with pytest.raises(Exception):
        twitter.tweet('test' * 41)
    assert twitter.tweet_messages == []


def test_initialize_two_twitter_classes(backend):
    twitter1 = Twitter(backend=backend)
    twitter2 = Twitter(backend=backend)

    twitter1.tweet('Test 1')
    twitter2.tweet('Test 2')

    assert twitter2.tweet_messages == ['Test 1', 'Test 2']


@pytest.mark.parametrize("message, expected", (
        ("Test #first message", ["first"]),
        ("#first test message", ["first"]),
        ("Test #First message", ["first"]),
        ("Test massage #first", ["first"]),
        ("Test message #first #second", ["first", "second"])
))
def test_tweet_with_hasztag(twitter, message, expected):
    assert twitter.find_hasztags(message) == expected


@patch.object(requests, 'get', return_value=ResponseGetMock())
def test_tweet_with_username(avatar_mock, twitter):
    if not twitter.username:
        pytest.skip()

    twitter.tweet('Test message')
    assert twitter.tweets == [{'message': 'Test message', 'avatar': 'test', 'hasztags': []}]
    avatar_mock.assert_called()


@patch.object(requests, 'get', return_value=ResponseGetMock())
def test_tweet_with_hasztag_mock(avatar_mock, twitter):
    twitter.find_hasztags = Mock()
    twitter.find_hasztags.return_value = ['first']
    twitter.tweet('Test #second')
    assert twitter.tweets[0]['hasztags'] == ['first']
    twitter.find_hasztags.assert_called_with('Test #second')


def getVersion():
    return '2.0'


def test_twitter_version(twitter):
    twitter.version = getVersion()
    assert twitter.version == '2.0'

