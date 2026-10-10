# HAIGC_VideoLoader

## 节点类型

`HAIGC_VideoLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `视频文件:COMBO`（1 次）
- `起始帧:INT`（1 次）
- `结束帧:INT`（1 次）
- `帧率:FLOAT`（1 次）
- `跳帧:INT`（1 次）
- `upload:IMAGEUPLOAD`（1 次）
- `视频路径:STRING`（1 次）
- `目标宽度:INT`（1 次）
- `目标高度:INT`（1 次）

## 输出

- `视频:IMAGE`（1 次）
- `音频:AUDIO`（1 次）
- `video_info:HAIGC_VIDEOINFO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["None", 0, 0, 0, 1, "image", "", 0, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
