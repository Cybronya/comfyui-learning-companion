# InfiniteYouApply

## 节点类型

`InfiniteYouApply`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `control_net:CONTROL_NET`（4 次）
- `model:MODEL`（4 次）
- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）
- `ref_image:IMAGE`（4 次）
- `latent_image:LATENT`（4 次）
- `vae:VAE`（4 次）

## 输出

- `MODEL:MODEL`（4 次）
- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）
- `latent:LATENT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["sim_stage1_img_proj.bin", "CUDA", 1.0000000000000002, 0, 1, false]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
