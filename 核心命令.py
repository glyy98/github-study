新建用户名和邮箱
git config user.name 'github用户名'
git config user.email '邮箱'

查看当前的用户名和邮箱
git config --global user.name
git config --global user.email添加远程仓库
git remote add 自定义仓库名 仓库地址

查看当前已添加的远程仓库
git remote -v   

删除已添加的远程仓库
git remote remove  origin  仓库名

查看当前仓库分支
git branch 


#在新的环境下载git后，会显示连接失败，是因为还没有给git配置你的本地代理
#33210这个是Sakuracat软件显示的端口
git config --global http.proxy http://127.0.0.1:33210
git config --global https.proxy http://127.0.0.1:33210

#如果要取消代理，使用以下命令
git config --global --unset http.proxy
git config --global --unset https.proxy

#设置git alias别名 给组合命令设置快捷命令

git config --global alias.pushall '!git add . && git commit -m "update" && git push'
【pushall】是可以自定义的
然后直接  git quick 
