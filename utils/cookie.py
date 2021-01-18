# -*- coding: utf-8 -*-
# Copyright (c) 2017-2020 Rhilip <rhilipruan@gmail.com>
# Licensed under the GNU General Public License v3.0

from http.cookies import SimpleCookie  # Python3 only （Py2: from Cookie import SimpleCookie）


def cookies_raw2jar(raw: str) -> dict:
    """
    Arrange Cookies from raw using SimpleCookies
    """
    if not raw:
        raise ValueError("The Cookies is not allowed to be empty.")

    cookie = SimpleCookie(raw)
    return {key: morsel.value for key, morsel in cookie.items()}
