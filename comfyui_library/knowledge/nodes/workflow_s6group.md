# workflow>S6Group

## 节点类型

`workflow>S6Group`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `CLIP:CLIP`（1 次）
- `图像:IMAGE`（1 次）
- `start_image:IMAGE`（1 次）
- `end_image:IMAGE`（1 次）
- `control_images:IMAGE`（1 次）
- `inpaint_mask:MASK`（1 次）
- `vae:VAE`（1 次）
- `reference_image:IMAGE`（1 次）
- `模型:MODEL`（1 次）
- `VAE:VAE`（1 次）

## 输出

- `批次大小:INT`（1 次）
- `通道:INT`（1 次）
- `trim_latent:INT`（1 次）
- `图像:IMAGE`（1 次）
- `GetImageRangeFromBatch 图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `ImageBatchMulti 图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Indoor setting. Soft ambient light. Camera shows the girl from head to heels. She stands poised. She wears glasses and`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
