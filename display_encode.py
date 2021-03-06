#!/usr/bin/env python
#coding=utf-8
 
import sys, locale
def SysCoding():
    fmt = '{0}: {1}'
    #当前系统所使用的默认字符编码
    print fmt.format('DefaultEncoding    ', sys.getdefaultencoding())
    #转换Unicode文件名至系统文件名时所用的编码('None'表示使用系统默认编码)
    print fmt.format('FileSystemEncoding ', sys.getfilesystemencoding())
    #默认的区域设置并返回元祖(语言, 编码)
    print fmt.format('DefaultLocale      ', locale.getdefaultlocale())
    #用户首选的文本数据编码(猜测结果)
    print fmt.format('PreferredEncoding  ', locale.getpreferredencoding())
    #解释器Shell标准输入字符编码
    print fmt.format('StdinEncoding      ', sys.stdin.encoding)
    #解释器Shell标准输出字符编码
    print fmt.format('StdoutEncoding     ', sys.stdout.encoding)

if __name__ == '__main__':
    SysCoding()    
