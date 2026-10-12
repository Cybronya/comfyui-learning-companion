# HAIGC_VideoResize

## 节点类型

`HAIGC_VideoResize`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `视频帧率:FLOAT`（1 次）
- `目标宽度:INT`（1 次）
- `目标高度:INT`（1 次）
- `缩放算法:COMBO`（1 次）

## 输出

- `视频:IMAGE`（1 次）
- `输出帧数:INT`（1 次）
- `输出时长:FLOAT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[30, 1920, 1080, "双三次"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
