import os,shutil

# # 获取当前文件的工作目录
# print(os.getcwd())
#
# # 修改当前工作路径
# os.chdir("/Users/zeroswift/Desktop")
# print(os.getcwd())
#
# # 获取系统目录
# print(os.environ['systemdrive'])
#
# # 获取用户目录
# print(os.environ['userprofile'])
#
# # 获取windows目录
# print(os.environ['windir'])

# # os.walk 遍历文件夹
# # 参数topdown的默认值是“True”表示首先返回顶级目录下的文件，然后再遍历子目录中的文件。
# # 当topdown的值为"False"时，表示先遍历子目录中的文件，然后再返回顶级目录下的文件。
# for root,dirs,file in os.walk("/Users/zeroswift/Desktop/myPython",topdown=False):
#     print(root) # /Users/zeroswift/Desktop/myPython
#     print(dirs) # ['.idea', 'clearWindosFile-py', 'winxosGameGrab-py']
#     print(file) #['.DS_Store']
#     print("--------------")

# # 对文件名进行切割
# fileContent = os.path.splitext(r'aaa\bbb\ccc.ddd')
# # 输出为('aaa\\bbb\\ccc', '.ddd')
# print(fileContent[1])

# # 删除文件
# os.remove("/Users/zeroswift/Desktop/myPython/testRemove.py")
# # 删除空文件夹
# os.rmdir("/Users/zeroswift/Desktop/myPython/testRemove")
# # 删除有数据的文件夹
# shutil.rmtree("/Users/zeroswift/Desktop/myPython/testRemove")

# 获取文件大小
# print(os.path.getsize("/Users/zeroswift/Desktop"))

# # 组合路径
# print(os.path.join("/Users/zeroswift/Desktop/myPath", "testAdd.py"))
