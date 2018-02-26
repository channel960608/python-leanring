#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_pailindrome(n):
    # return str(n)[::-1] == str(n)
    return int(str(n)[::-1])==n

print(list(filter(is_pailindrome, range(1, 1000))))
