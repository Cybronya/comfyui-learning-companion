# LatentSyncNode

## 节点类型

`LatentSyncNode`

## 分类

Latent

## 作用

latent 空间处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `audio:AUDIO`（1 次）
- `seed:INT`（1 次）
- `lips_expression:FLOAT`（1 次）
- `inference_steps:INT`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[85, "randomize", 1.5, 20]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
