# InpaintModelConditioning

## 节点类型

`InpaintModelConditioning`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `positive:CONDITIONING`（10 次）
- `negative:CONDITIONING`（10 次）
- `vae:VAE`（10 次）
- `pixels:IMAGE`（10 次）
- `mask:MASK`（10 次）
- `noise_mask:BOOLEAN`（10 次）

## 输出

- `positive:CONDITIONING`（10 次）
- `negative:CONDITIONING`（10 次）
- `latent:LATENT`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false]`（6 次）
- `[true]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
