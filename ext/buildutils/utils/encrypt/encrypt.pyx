# cython: language_level=3
import os
import base64
from typing import List, Optional, Union
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


ctypedef fused BytesData:
    bytes
    List[int]
    str
    


"""自定义数据类型，iv、plain、cipher 都可以使用此类型"""


cdef class AESencrypt:
    
    cpdef bytes to_bytes(self, src):
        if isinstance(src, bytes):
            return src
        elif isinstance(src, str):
            return src.encode()
        elif isinstance(src, list):
            return bytes(src)
        else:
            return src

    
    cpdef bytes generate_iv(self):
        """生成一个随机 iv（伪随机）"""
        return os.urandom(16)
    
    cpdef bytes generate_key(self,int length = 16) :
        """
            生成一个随机的密钥
        :param length 密钥长度,默认为16字节
        """
        return get_random_bytes(length)
    cpdef tuple encrypt(self, str plain,bytes key):
        """加密

        Parameters
        ----------
        plain : str
            待加密的明文
    key : str
        Returns
        -------
        tuple(bytes, bytes)
            返回密文 bytes 和生成的 iv。
        """
        iv = self.generate_iv()

        cipher = AES.new(key, AES.MODE_CBC, iv)

        cipher_data = cipher.encrypt(pad(plain.encode(), AES.block_size))

        return cipher_data, iv
    cpdef bytes decrypt(self,BytesData cipher_data,BytesData iv_data,bytes key):
        """解密

        Parameters
        ----------
        cipher_data : BytesData
            多个类型的密文。
        iv_data : BytesData
            iv 数据，如果你没有改代码，类型应该就是 bytes。

            当然你也可以传入 str、list[int]类型的数据。
        key : str

        Returns
        -------
        bytes
            明文 bytes。
        """
        cipher = AES.new(key, AES.MODE_CBC, self.to_bytes(iv_data))

        plain_data = cipher.decrypt(self.to_bytes(cipher_data))

        return unpad(plain_data, AES.block_size)


    cpdef list[int] to_byte_array(self,bytes src):
        """将 bytes 转换成 list[int]，与 rust 对比用的函数，你可以删掉"""
        return [i for i in src]
    
    cpdef str bytes2b64(self,bytes  b):
        return base64.b64encode(b).decode("utf-8")
    
    cpdef bytes b642bytes(self,str b64):
        return base64.b64decode(b64)
    cpdef tuple encrypt_b64(self,str plain,bytes key):
        """加密

        Parameters
        ----------
        plain : str
            待加密的明文
    key :   str
        Returns
        -------
        tuple(str, bytes)
            返回密文 base64 和生成的 iv。
        """
        iv = self.generate_iv()

        cipher = AES.new(key, AES.MODE_CBC, iv)

        cipher_data = cipher.encrypt(pad(plain.encode(), AES.block_size))

        return self.bytes2b64(cipher_data), iv
    cpdef str decrypt_b64(self,str cipher_data,BytesData iv_data,bytes key):
        """解密

        Parameters
        ----------
        cipher_data : str
            base64
        iv_data : BytesData
            iv 数据，如果你没有改代码，类型应该就是 bytes。
        key :: str

            当然你也可以传入 str、list[int]类型的数据。

        Returns
        -------
        str
            明文 str。
        """
        cipher = AES.new(key, AES.MODE_CBC, self.to_bytes(iv_data))

        plain_data = cipher.decrypt(self.to_bytes(self.b642bytes(cipher_data)))

        return unpad(plain_data, AES.block_size).decode()
