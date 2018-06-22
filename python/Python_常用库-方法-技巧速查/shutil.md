# shutil模块

## 简介

> It means "shell utilities", sh standing for shell, util standing for utilities.
>
> If you think about what shutil does, that makes sense (manipulate the filesystem, make archives, etc.).

The [`shutil`](#module-shutil) module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal. For operations on individual files, see also the [`os`](os.html#module-os) module.

## 使用

```python
# hutil.copyfileobj(fsrc, fdst[, length])
# 将文件内容拷贝到另一个文件中
import shutil
shutil.copyfileobj(open('old.xml','r'), open('new.xml', 'w'))

#shutil.copyfile(src, dst)
#拷贝文件
shutil.copyfile('f1.log', 'f2.log')

#shutil.copymode(src, dst)
#仅拷贝权限。内容、组、用户均不变
shutil.copymode('f1.log', 'f2.log')

#shutil.copystat(src, dst)
#仅拷贝状态的信息，包括：mode bits, atime, mtime, flags
shutil.copystat('f1.log', 'f2.log')

#shutil.copy(src, dst)
#拷贝文件和权限
shutil.copy('f1.log', 'f2.log')

#shutil.copy2(src, dst)
#拷贝文件和状态信息
shutil.copy2('f1.log', 'f2.log')

#shutil.ignore_patterns(*patterns)
#shutil.copytree(src, dst, symlinks=False, ignore=None)
#递归的去拷贝文件夹
shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))
shutil.copytree('f1', 'f2', symlinks=True, ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))

#shutil.rmtree(path[, ignore_errors[, onerror]])
#递归的去删除文件
shutil.rmtree('folder1')

#shutil.move(src, dst)
#递归的去移动文件，它类似mv命令，其实就是重命名。
shutil.move('folder1', 'folder3')

#shutil.make_archive(base_name, format,...)
#创建压缩包并返回文件路径，例如：zip、tar
#创建压缩包并返回文件路径，例如：zip、tar
    #base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
        #如：www =>保存至当前路径
        #如：/Users/wupeiqi/www =>保存至/Users/wupeiqi/
    #format：	压缩包种类，“zip”, “tar”, “bztar”，“gztar”
    #root_dir：	要压缩的文件夹路径（默认当前目录）
    #owner：	用户，默认当前用户
    #group：	组，默认当前组
    #logger：	用于记录日志，通常是logging.Logger对象

#将 /Users/wupeiqi/Downloads/test 下的文件打包放置当前程序目录
import shutil
ret = shutil.make_archive("wwwwwwwwww", 'gztar', root_dir='/Users/wupeiqi/Downloads/test')
   
#将 /Users/wupeiqi/Downloads/test 下的文件打包放置 /Users/wupeiqi/目录
import shutil
ret = shutil.make_archive("/Users/wupeiqi/wwwwwwwwww", 'gztar', root_dir='/Users/wupeiqi/Downloads/test')

# ===================
#shutil 对压缩包的处理是通过调用ZipFile 和 TarFile两个模块来进行的。

import zipfile
# 压缩
z = zipfile.ZipFile('laxi.zip', 'w')
z.write('a.log')
z.write('data.data')
z.close()
# 解压
z = zipfile.ZipFile('laxi.zip', 'r')
z.extractall()
z.close()

import tarfile
# 压缩
tar = tarfile.open('your.tar','w')
tar.add('/Users/wupeiqi/PycharmProjects/bbs2.log', arcname='bbs2.log')
tar.add('/Users/wupeiqi/PycharmProjects/cmdb.log', arcname='cmdb.log')
tar.close()
# 解压
tar = tarfile.open('your.tar','r')
tar.extractall()  # 可设置解压地址
tar.close()
```

