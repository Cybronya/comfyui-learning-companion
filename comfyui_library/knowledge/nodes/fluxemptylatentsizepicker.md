# FluxEmptyLatentSizePicker

## 节点类型

`FluxEmptyLatentSizePicker`

## 分类

Latent

## 作用

latent 空间处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `resolution:COMBO`（1 次）
- `batch_size:INT`（1 次）
- `width_override:INT`（1 次）
- `height_override:INT`（1 次）

## 输出

- `LATENT:LATENT`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["832x1152 (0.96MP) - 3:4", 1, 0, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
