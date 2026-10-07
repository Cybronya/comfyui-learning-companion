# Flex2Conditioner

## 节点类型

`Flex2Conditioner`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 13 个 workflow 中。

## 输入

- `model:MODEL`（19 次）
- `vae:VAE`（19 次）
- `positive:CONDITIONING`（19 次）
- `negative:CONDITIONING`（19 次）
- `latent:LATENT`（19 次）
- `inpaint_image:IMAGE`（19 次）
- `inpaint_mask:MASK`（19 次）
- `control_image:IMAGE`（19 次）

## 输出

- `model:MODEL`（19 次）
- `positive:CONDITIONING`（19 次）
- `negative:CONDITIONING`（19 次）
- `latent:LATENT`（19 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["no", 3.5, 0.5000000000000001, 0, 0.7000000000000002]`（5 次）
- `["no", 3.5, 1, 0, 1]`（3 次）
- `["no", 3.5, 1.0000000000000002, 0, 1]`（3 次）
- `["no", 3.5, 0.7500000000000001, 0, 1]`（2 次）
- `["no", 3.5, 0.5000000000000001, 0, 0.8000000000000002]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
