# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:19:22 2020

@author: guilh
"""

from main import get_temperature
import pytest
import requests


class MockResponse:

    @staticmethod
    def json():
        return {'currently': {'temperature': 62}}
    
    
@pytest.mark.parametrize('lat, lng, expected', [(-14.235004, -51.92528, 16)])
def test_get_temperature(monkeypatch, lat, lng, expected):

    def mock_get(*args, **kwargs):
        return MockResponse()
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    result = get_temperature(lat, lng)
    
    assert result == expected
