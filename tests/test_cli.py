# -*- coding: utf-8 -*-
from lugatim_cli.cli import get_cookie
from lugatim_cli.cli import get_results


def test_get_cookie():
    assert get_cookie() != "Session error!"


def test_get_results():
    assert get_results("kemalizm") == ["KEMALİZM", ["i. Atatürkçülük."]]
