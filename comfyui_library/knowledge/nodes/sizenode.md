# SizeNode

## 节点类型

`SizeNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `size_mode:COMBO`（2 次）
- `aspect_ratio:COMBO`（2 次）
- `custom_width:INT`（2 次）
- `custom_height:INT`（2 次）
- `batch_size:INT`（2 次）

## 输出

- `latent:LATENT`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["custom", "1:1", 768, 1024, 4]`（1 次）
- `["custom", "1:1", 768, 1280, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
