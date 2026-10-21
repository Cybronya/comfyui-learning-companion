# GetLatentSize

## 节点类型

`GetLatentSize`

## 分类

Latent

## 作用

latent 空间处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `latent:LATENT`（4 次）

## 输出

- `width:INT`（4 次）
- `height:INT`（4 次）
- `frames:INT`（4 次）
- `batch_size:INT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["width: 68, height: 120\n frames: 1, batch size: 11937e6b6a61c907e37cb6cc88a627e2e"]`（1 次）
- `["width: 105, height: 128\n frames: 1, batch size: 17c674851355d2a3d910e84d7a3a3d300"]`（1 次）
- `[]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
