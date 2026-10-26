# LLAIDownloadVideo

## 节点类型

`LLAIDownloadVideo`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `video_url:STRING`（3 次）
- `save_dir:STRING`（3 次）
- `filename:STRING`（3 次）
- `timeout:INT`（3 次）

## 输出

- `本地路径:STRING`（3 次）
- `状态:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["https://jisuchuan.com/api/data/download?key=5a3bcce25ff4468345efa57da25ed5d3.safetensors&name=clip_00001.safetensors",`（2 次）
- `["https://rh-images-tos.xiaoyaoyou.com/cc54d14dd440fe29a6dafe9080e40e26/output/h3_context/clip_00001_ooppb_1792928140.sa`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
