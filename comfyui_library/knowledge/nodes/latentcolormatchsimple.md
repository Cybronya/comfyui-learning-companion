# LatentColorMatchSimple

## 节点类型

`LatentColorMatchSimple`

## 分类

Latent

## 作用

latent 空间处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `latent:LATENT`（2 次）
- `reference:LATENT`（2 次）
- `method:COMBO`（2 次）
- `strength:FLOAT`（2 次）
- `device:COMBO`（2 次）

## 输出

- `LATENT:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["channel_wise", 0.2, "auto"]`（1 次）
- `["channel_wise", 0.30000000000000004, "auto"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
