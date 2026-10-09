# PerturbedAttention

## 节点类型

`PerturbedAttention`

## 分类

Optimization

## 作用

注意力/加速优化节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `scale:FLOAT`（1 次）
- `adaptive_scale:FLOAT`（1 次）
- `unet_block:COMBO`（1 次）
- `unet_block_id:INT`（1 次）
- `sigma_start:FLOAT`（1 次）
- `sigma_end:FLOAT`（1 次）
- `rescale:FLOAT`（1 次）
- `rescale_mode:COMBO`（1 次）
- `unet_block_list:STRING`（1 次）

## 输出

- `MODEL:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 0.1, "middle", 0, -1, -1, 0, "full", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
