# ACEPlusConditioning

## 节点类型

`ACEPlusConditioning`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）
- `vae:VAE`（4 次）
- `ucpixels:IMAGE`（4 次）
- `cpixels:IMAGE`（4 次）
- `mask:MASK`（4 次）

## 输出

- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）
- `latent:LATENT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
