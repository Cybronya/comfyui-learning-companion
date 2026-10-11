# HAIGC_VideoLastFrame

## 节点类型

`HAIGC_VideoLastFrame`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `提取模式:COMBO`（1 次）
- `帧数N:INT`（1 次）
- `重复输出次数:INT`（1 次）
- `输出帧信息:BOOLEAN`（1 次）

## 输出

- `尾帧图像:IMAGE`（1 次）
- `总帧数:INT`（1 次）
- `提取帧数:INT`（1 次）
- `输出帧数:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["最后一帧", 1, 1, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
