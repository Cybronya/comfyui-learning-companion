# PowerPaint

## 节点类型

`PowerPaint`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 10 个 workflow 中。

## 输入

- `model:MODEL`（10 次）
- `vae:VAE`（10 次）
- `image:IMAGE`（10 次）
- `mask:MASK`（10 次）
- `powerpaint:BRMODEL`（10 次）
- `clip:CLIP`（10 次）
- `positive:CONDITIONING`（10 次）
- `negative:CONDITIONING`（10 次）

## 输出

- `model:MODEL`（10 次）
- `positive:CONDITIONING`（10 次）
- `negative:CONDITIONING`（10 次）
- `latent:LATENT`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, "object removal", 1, 0, 10000, "none"]`（6 次）
- `[1, "image outpainting", 1, 0, 10000, "auto"]`（1 次）
- `[1, "image outpainting", 1, 0, 10000, "none"]`（1 次）
- `[1, "context aware", 1, 0, 10000, "none"]`（1 次）
- `[1, "text guided", 1, 0, 10000, "none"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
