# HAIGC_VideoRelay

## 节点类型

`HAIGC_VideoRelay`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `视频:VIDEO`（1 次）
- `每隔N帧:INT`（1 次）
- `最大帧数:INT`（1 次）

## 输出

- `帧:IMAGE`（1 次）
- `音频:AUDIO`（1 次）
- `视频信息:HAIGC_VIDEOINFO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[15, 9]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
