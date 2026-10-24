# BRIAAI Matting

## 节点类型

`BRIAAI Matting`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video_frames:IMAGE`（3 次）
- `version:COMBO`（3 次）
- `fp16:BOOLEAN`（3 次）
- `bg_color:STRING`（3 次）
- `batch_size:INT`（3 次）

## 输出

- `IMAGE:IMAGE`（3 次）
- `MASK:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["v1.4", true, "white", 4]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
