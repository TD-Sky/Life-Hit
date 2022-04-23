# Life Hit：B站生活区热榜视频弹幕爬虫

## 依赖

- scrapy
- numpy
- matplotlib
- jieba
- wordcloud



## 运行

```bash
$ python3 main.py
```



## 注意事项

- `life_hit/settings.py`：`USER_AGENT`字段要换成你主机的；我写的是Linux路径格式，没做跨平台，因为目前已知方法不够简洁。

- 日志会生成到`cache`目录。

