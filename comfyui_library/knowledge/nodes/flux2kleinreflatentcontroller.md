# Flux2KleinRefLatentController

## 节点类型

`Flux2KleinRefLatentController`

## 分类

Latent

## 作用

latent 空间处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（6 次）
- `conditioning:CONDITIONING`（6 次）
- `strength:FLOAT`（6 次）
- `reference_index:INT`（6 次）
- `spatial_fade:COMBO`（6 次）
- `spatial_fade_strength:FLOAT`（6 次）
- `debug:BOOLEAN`（6 次）

## 输出

- `MODEL:MODEL`（6 次）
- `CONDITIONING:CONDITIONING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2.2, 0, "none", 0.5, true]`（3 次）
- `[2, 1, "none", 0.5, true]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
