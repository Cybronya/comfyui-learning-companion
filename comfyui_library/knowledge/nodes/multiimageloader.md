# MultiImageLoader

## 节点类型

`MultiImageLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image_paths:STRING`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `interpolation:COMBO`（2 次）
- `resize_method:COMBO`（2 次）
- `multiple_of:INT`（2 次）
- `img_compression:INT`（2 次）

## 输出

- `multi_output:IMAGE`（2 次）
- `image_1:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 1280, 720, "lanczos", "keep proportion", 16, 18, ""]`（1 次）
- `["d197544b67e656855c4f32801ca369b9aab0c3b6c2340c73856195bd798909a5.png", 0, 0, "lanczos", "crop", 0, 18, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
