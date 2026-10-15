# LTXReferenceConditioning

## 节点类型

`LTXReferenceConditioning`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `vae:VAE`（2 次）
- `image:IMAGE`（2 次）
- `target_latent:LATENT`（2 次）
- `strength:FLOAT`（2 次）
- `position_mode:COMBO`（2 次）
- `verbose:BOOLEAN`（2 次）

## 输出

- `model:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, "reference", false]`（1 次）
- `[0, "reference", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
