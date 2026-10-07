# workflow>MainLoad

## 节点类型

`workflow>MainLoad`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `ckpt_name:COMBO`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `swap_dimensions:COMBO`（1 次）
- `upscale_factor:FLOAT`（1 次）
- `batch_size:INT`（1 次）

## 输出

- `模型:MODEL`（1 次）
- `CLIP:CLIP`（1 次）
- `VAE:VAE`（1 次）
- `放大系数:FLOAT`（1 次）
- `empty_latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["waiNSFWIllustrious_v140.safetensors", 1024, 1024, "16:9 landscape 1344x768", "Off", 2, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
