# HAIGC_VideoTrim

## 节点类型

`HAIGC_VideoTrim`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `audio:AUDIO`（1 次）
- `视频帧率:FLOAT`（1 次）
- `裁剪模式:COMBO`（1 次）
- `开始时间:FLOAT`（1 次）
- `结束时间:FLOAT`（1 次）
- `开始帧:INT`（1 次）
- `结束帧:INT`（1 次）

## 输出

- `视频:IMAGE`（1 次）
- `音频:AUDIO`（1 次）
- `输出帧数:INT`（1 次）
- `输出时长:FLOAT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[30, "按帧数", 0, 0, 0, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
