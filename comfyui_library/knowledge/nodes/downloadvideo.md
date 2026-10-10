# DownloadVideo

## 节点类型

`DownloadVideo`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video_url:STRING`（1 次）
- `save_dir:STRING`（1 次）
- `filename:STRING`（1 次）
- `timeout:INT`（1 次）

## 输出

- `本地路径:STRING`（1 次）
- `状态:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "output/sora2", "", 200]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
