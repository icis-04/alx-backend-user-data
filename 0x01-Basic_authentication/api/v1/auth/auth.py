#!/usr/bin/env python3
""" script that implements Authorization in flask"""
from flask import request


class Auth:
    """ BAsic Auth class name """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ function that makes sure a path requires auth """
        self.path = path
        self.excluded_paths = excluded_paths
        return False
    def authorization_header(self, request=None) -> str:
        """ function that handles the authorization header """
        self.request = request
        return None
    def current_user(self, request=None) -> TypeVar('User'):
        """ return who the user is """
        self.request = request
        return None
