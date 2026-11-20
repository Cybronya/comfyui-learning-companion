# WanEx_VideoColorMatch

## 节点类型

`WanEx_VideoColorMatch`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `reference:IMAGE`（1 次）
- `reference_mask:MASK`（1 次）
- `target_index:INT`（1 次）
- `reference_index:INT`（1 次）
- `color_space:COMBO`（1 次）
- `factor:FLOAT`（1 次）
- `device:COMBO`（1 次）
- `batch_size:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, -1, "LAB", 1, "auto", 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
