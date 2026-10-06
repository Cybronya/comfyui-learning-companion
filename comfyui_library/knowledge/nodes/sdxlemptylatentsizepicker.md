# SDXLEmptyLatentSizePicker+

## 节点类型

`SDXLEmptyLatentSizePicker+`

## 分类

Latent

## 作用

latent 空间处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `resolution:COMBO`（5 次）
- `batch_size:INT`（5 次）
- `width_override:INT`（5 次）
- `height_override:INT`（5 次）

## 输出

- `LATENT:LATENT`（5 次）
- `width:INT`（5 次）
- `height:INT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["1024x1024 (1.0)", 1, 1024, 1024]`（3 次）
- `["1024x1024 (1.0)", 1, 2048, 1024]`（1 次）
- `["1024x1024 (1.0)", 1, 1920, 1088]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
