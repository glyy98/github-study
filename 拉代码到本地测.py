#一般是先把main分支的包全部下载
1、已下载了main分支的包，用vscode打开
2、创建并切换到子分支
git switch -c qian-gang 
3、将迁钢的代码拉下来更新
git pull origin qian-gang

------------之前填写的注意事项---------------
从gitlab上拉代码到本地测试，需要注意的几点
1、是否安装了node.js，没装就去官网安装
2、查看node 版本  node -v
3、安装pnpm    npm install pnpm -g
4、然后在本地将项目包clone下来
git clone  http地址
在项目包里打开终端   pnpm  dev  运行项目    
[图片]
5、在vscode打开项目包  左下角有分支可以切换  
[图片]
6、注意切换分支后再重新打开一个浏览器窗口   避免浏览器缓存
7、在这个  vite.config.ts  文件中   可以更改项目环境  鞍钢/酒钢/    双//表示注释
[图片]
8、切换分支记得重新拉一次代码：git pull 
如果开vpn会导致无法访问gitlab，解决办法：在windows配置域名不使用代理
[图片]