# 小米手机提取微信聊天记录数据库（qq聊天记录）并将与特定好友的聊天记录提取成词云展示

[参考项目提取聊天记录](https://github.com/Heyxk/notes/tree/master)

[参考项目生成词云](https://github.com/godweiyang/wordcloud)

本文的最终目的是将手机微信（电脑端qq）的聊天记录导出到电脑里，变成txt文本文件，然后对其进行分析。

- resource中是破解数据库的文件
- wordCloud中是词云展示的文件



2023.5.20增加的内容

- 微信聊天数据库破解
- 将聊天记录文件进行词云展示



## 1.微信聊天

```
手机：小米11pro
系统：miui14.0.6
```

小米手机做法很简单，不需要进行root。（雷总、金凡！！！dbq骂习惯了嘿嘿）

1. 首先进入手机的`设置-我的设备-备份与恢复-手机备份恢复`，输入密码，点击`立即备份`，把微信的内容选择，，点击确定，点击开始备份，等待完成就行了

2. 将手机连接到电脑，打开手机目录`MIUI/backup/AllBackup/yyyymmdd_xxxxxx/`文件夹，将`.bak`文件拷贝到电脑上，我这里重命名为了`fxk.bak`。

   ![](https://oss-img-fxk.oss-cn-beijing.aliyuncs.com/markdown/image-20230520230431450.png)

3. 然后用任意一种压缩包软件（推荐使用[7zip](https://www.7-zip.org/download.html)）打开这个`fxk.bak`文件，并且将

   ```
   \fxk.bak\apps\com.tencent.mm\r\MicroMsg\xxxx\EnMocroMsg.db
   \fxk.bak\apps\com.tencent.mm\r\MicroMsg\systemInfo.cfg
   \fxk.bak\apps\com.tencent.mm\r\MicroMsg\CompatibleInfo.cfg
   ```

   三个文件解压到电脑上。这里xxxx是一串随机的字母，代表你的微信用户，每个人不一样，一般是最大的那个文件夹.

4. 将'resource/wechat-tools'目录下面的文件放到上面三个文件的同一个目录下面。

   ![image-20230520231534798](https://oss-img-fxk.oss-cn-beijing.aliyuncs.com/markdown/image-20230520231534798.png)

5. 然后命令行运行如下代码：

   ```text
   javac IMEI.java
   java IMEI systemInfo.cfg CompatibleInfo.cfg
   ```

   第三行就是数据库的密码了。

   ![image-20230520231624888](https://oss-img-fxk.oss-cn-beijing.aliyuncs.com/markdown/image-20230520231624888.png)

6. 然后打开`sqlcipher.exe`软件，用它打开`EnMicroMsg.db`数据库，输入第五步得到的密码。

7. 这时候会显示出很多的表格，点击菜单栏的`File-Export-Table as CSV file`，选择`message`表，并导出。

   ![image-20230520231842404](https://oss-img-fxk.oss-cn-beijing.aliyuncs.com/markdown/image-20230520231842404.png)

   ![image-20230520232237904](https://oss-img-fxk.oss-cn-beijing.aliyuncs.com/markdown/image-20230520232237904.png)

8. 如果直接用excel打开`.csv`文件。根据聊天记录查找自己朋友的talker。

   content是聊天内容--根据这个找到朋友的talker。

   ![image-20230520232901390](https://oss-img-fxk.oss-cn-beijing.aliyuncs.com/markdown/image-20230520232901390.png)

9. 然后使用preprocess_wx.py根据talker提取对映的朋友的聊天记录。

   ```
   # 朋友或者群聊的id
   TALKER = ""
   # 聊天记录csv文件的地址
   MESSAGES_PATH = ""
   ```

10. 使用create_word_cloud.py生成词云。

    `python  create_word_cloud.py filename.txt`



## 2.QQ聊天记录

- qq消息管理选择对映好友的聊天记录进行导出txt格式

- 运行preprocess_qq.py

  ```
  # txt文件的目录
  QQ_FILE_PATH = ""
  # txt文件的文件名
  FILE_NAME = ""
  ```

- 使用create_word_cloud.py生成词云。

  `python  create_word_cloud.py filename.txt`