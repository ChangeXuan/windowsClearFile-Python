import json
import os
import shutil
from pip._vendor.distlib.compat import raw_input

delExtension = {
 '.tmp': '临时文件',
 '._mp': '临时文件_mp',
 '.log': '日志文件',
 '.gid': '临时帮助文件',
 '.chk': '磁盘检查文件',
 '.old': '临时备份文件',
 '.xlk': 'Excel备份文件',
 '.bak': '临时备份文件bak'
}

# 获取用户目录
USERPROFILE = os.environ['userprofile']

class DiskClearn(object):
    # 初始化类
    def __init__(self):
        self.delInfo = {}
        self.delPath = []
        self.sumSize = 0
        for k,v in delExtension.items():
            self.delInfo[k] = dict(name=v,count=0)
        pass

    # 扫描磁盘
    def scanDisk(self):
        for roots, dirs, files in os.walk(USERPROFILE, topdown=False):
            # 生成并展开以 root 为根目录的目录树，参数 topdown 设定展开方式从底层到顶层
            for fileItem in files:
                # 获取扩展名
                fileExtension = os.path.splitext(fileItem)[1]
                if fileExtension in self.delInfo:
                    # 文件完整路径
                    fileFullPath = os.path.join(roots, fileItem)
                    self.delPath.append(fileFullPath)
                    self.delInfo[fileExtension]['count'] += 1
                    self.sumSize += os.path.getsize(fileFullPath)
        pass

    # 显示删除文件的信息
    def showDelDisk(self):
        # 因为python的dumps会把中文变成这种格式"\u535a\u5ba2\u56ed"输出
        # 所以要输出中文需要指定ensure_ascii参数为False
        # indent是缩进
        print(json.dumps(self.delInfo, indent=4, ensure_ascii=False))
        print('删除可节省:%s kb空间' % self.total_size)
        pass

    # 从路径中选取文件path
    def delFiles(self):
        for delFilePath in self.delPath:
            self.delDirOrFile(delFilePath)
        pass

    # 删除的实际操作
    def delDirOrFile(root):
        try:
            if os.path.isfile(root):
                # 删除文件
                os.remove(root)
                print('file: ' + root + ' removed')
            elif os.path.isdir(root):
                # 删除文件夹
                shutil.rmtree(root)
                print('directory: ' + root + ' removed')
        except WindowsError:
            print('failure: ' + root + " can't remove")


if __name__ == "__main__":
    helloClearn = DiskClearn()
    helloClearn.scanDisk()
    helloClearn.showDelDisk()
    if raw_input('是否删除y/n:') == 'y':
        helloClearn.delFiles()
    pass