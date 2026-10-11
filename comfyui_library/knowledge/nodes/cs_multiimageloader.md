# CS-MultiImageLoader

## 节点类型

`CS-MultiImageLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image_paths:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `interpolation:COMBO`（1 次）
- `resize_method:COMBO`（1 次）
- `multiple_of:INT`（1 次）
- `img_compression:INT`（1 次）

## 输出

- `multi_output:IMAGE`（1 次）
- `image_1:IMAGE`（1 次）
- `image_2:IMAGE`（1 次）
- `image_3:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["c2c0d3bbe6b8d7221aa2fecb1cba9e5b80adef6f027a216a2a550113aaddcef7.png\ne00549deaec6c4f471cf439c51473ac287fc8dc41afad784`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
