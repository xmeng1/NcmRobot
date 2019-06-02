# Ncm Robot

This python project is design for convert the ncm file to the mp3 file automatically based on existing ncm dump tools such as:

[anonymous5l/ncmdump](https://github.com/anonymous5l/ncmdump)
[ncmdump.go](https://github.com/yoki123/ncmdump/)


## How it works?

We download ncm everyday, and if we use these tools directly, we need to convert these ncm file directly. So this tool will help to convert the files easier.

### Command Line Version

User only need one line command and convert all new downloaded ncm music.

1. Setup the NetEase Music Folder such as the default: `/Users/YOUR_USER_NAME/Music/网易云音乐`
2. Initial list all the ncm file in the folder and start to convert the files to mp3 automatically.
3. Remember the latest music time stamp.
4. Next time run the command, check the last `latest music time stamp` and only convert the file newer than the timestamp. If cannot find it, just convert all ncm files. Then Update the lasted time stamp.
5. Add Automatically task to run the command every days or just manually run it when you finish to download the ncm music or prepare to copy the mp3 to your devices.

#### Python technique

1. how to run the command line
2. how to list file with specific file name and filter out by time stamp
3. how to read/write time stamp to file
4. how to compile python to execute file


## Ref

https://www.zhihu.com/question/266369267
http://www.bewindoweb.com/228.html
https://github.com/yoki123/ncmdump
https://github.com/anonymous5l/ncmdump
https://www.yanghuaxing.com/blog/107.html

