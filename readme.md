#一级题标
##二级标题

- 打开
- 关闭
1. 开门
2. 进来
3. 关门

[百度](www.baidu.com)

>##长风破浪

![tu](http://p1.img.cctvpic.com/photoworkspace/contentimg/2017/09/11/2017091100290896168.jpg)

**粗体**

*斜体*

```buildoutcfg
def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request,'blog/index.html',context={'post_list':post_list})
```