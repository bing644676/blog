#!/usr/bin/env/ python3
# -*- coding:utf-8 -*-
"""
@Project: serve-blog
@File  :auth.py
@Author:zy7y
@Date  :2021/6/10 19:49
@Desc  :
"""
from typing import List, Union

from fastapi import APIRouter, Depends

import core
from db import models

auth = APIRouter(tags=["登录相关"])


@auth.post("/login", name="登录")
async def login(user: core.Login):
    try:
        user_obj = await models.User.get(username=user.username)
        if user_obj and core.verify_password(user.password, user_obj.password):
            return core.Success(data=core.Token(
                token=core.create_access_token({"sub": user_obj.username})))
    except Exception as e:
        pass
    return core.Fail(message="用户名或密码错误")


@auth.post("/logout", name="退出")
async def logout(token: str = Depends(core.get_current_user)):
    return core.Success(data=token)
