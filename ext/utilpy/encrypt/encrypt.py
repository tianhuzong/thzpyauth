import os
import base64
from typing import List, Optional, Union
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

BytesData = Union[List[int], str, bytes]
"""自定义数据类型，iv、plain、cipher 都可以使用此类型"""


class AESencrypt:
    @staticmethod
    def to_bytes(src: BytesData) -> bytes:
        """将一些其他类型的数据转换成 bytes"""
        if isinstance(src, list):
            return bytes(src)

        if isinstance(src, str):
            return src.encode()

        return src

    @staticmethod
    def generate_iv() -> bytes:
        """生成一个随机 iv（伪随机）"""
        return os.urandom(16)
    @staticmethod
    def generate_key(length: int = 16) -> bytes:
        """
            生成一个随机的密钥
        :param length 密钥长度,默认为16字节
        """
        return get_random_bytes(length)
    def encrypt(self, plain: str,key : bytes):
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
    def decrypt(self, cipher_data: BytesData, iv_data: BytesData,key : bytes):
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

    @staticmethod
    def to_byte_array(src: bytes):
        """将 bytes 转换成 list[int]，与 rust 对比用的函数，你可以删掉"""
        return [i for i in src]
    @staticmethod
    def bytes2b64(b : bytes):
        return base64.b64encode(b).decode("utf-8")
    @staticmethod
    def b642bytes(b64 : str):
        return base64.b64decode(b64)
    def encrypt_b64(self, plain: str,key : bytes):
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

        return bytes2b64(cipher_data), iv
    def decrypt_b64(self, cipher_data: str, iv_data: BytesData,key : bytes):
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
        bytes
            明文 bytes。
        """
        cipher = AES.new(key, AES.MODE_CBC, self.to_bytes(iv_data))

        plain_data = cipher.decrypt(self.to_bytes(b642bytes(cipher_data)))

        return unpad(plain_data, AES.block_size).decode()
