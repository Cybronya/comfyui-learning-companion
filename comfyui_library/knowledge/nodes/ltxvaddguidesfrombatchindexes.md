# LTXVAddGuidesFromBatchIndexes

## 节点类型

`LTXVAddGuidesFromBatchIndexes`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `positive:CONDITIONING`（15 次）
- `negative:CONDITIONING`（15 次）
- `vae:VAE`（15 次）
- `latent:LATENT`（15 次）
- `images:IMAGE`（15 次）
- `img_compression:INT`（15 次）
- `image_indexes:STRING`（15 次）
- `strength:FLOAT`（15 次）

## 输出

- `positive:CONDITIONING`（15 次）
- `negative:CONDITIONING`（15 次）
- `latent:LATENT`（15 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, "", 1]`（11 次）
- `[18, "", 1]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
