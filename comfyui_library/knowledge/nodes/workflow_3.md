# workflow>3

## 节点类型

`workflow>3`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `Image Resize image:IMAGE`（1 次）
- `mask1:MASK`（1 次）
- `mask2:MASK`（1 次）
- `image3:IMAGE`（1 次）
- `mask3:MASK`（1 次）
- `image4:IMAGE`（1 次）
- `mask4:MASK`（1 次）
- `image5:IMAGE`（1 次）
- `mask5:MASK`（1 次）

## 输出

- `tools:BOOLEAN`（1 次）
- `batch_size:INT`（1 次）
- `config:COMPOSITOR_CONFIG`（1 次）
- `extendedConfig:COMPOSITOR_CONFIG`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["rescale", "true", "lanczos", 0.5000000000000001, 1024, 1536, "rescale", "true", "lanczos", 1.0000000000000002, 1024, 1`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
