#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
        �Q��AI�Ʉۻ�VI��S1�6���T���������{T��W:�7A���ݭc�n"�Ix\^��L�y�(����U�E�9n+�^v+��O ���`�
�Œ_����������d.'�GdGɽ՞"""
from hashlib import sha256
if(sha256(blob).hexdigest()=="6b45cf44537b11f55e9afda794db5d90f04d55d6fd13abad48da3445cc3c04b6"):
	print("I come in peace.")
elif(sha256(blob).hexdigest() =="b483c917dec661ee1d4f0e2486e5b3d8c726223c03c501b52d84a66f057779ab"):
	print("Prepare to be destroyed!")
