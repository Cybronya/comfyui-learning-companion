# workflow>main

## 节点类型

`workflow>main`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `CONDITIONING:CONDITIONING`（1 次）
- `VAE:VAE`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `batch_size:INT`（1 次）
- `unet_name:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）
- `seed:INT`（1 次）
- `steps:INT`（1 次）
- `cfg:FLOAT`（1 次）

## 输出

- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 512, 1, "Flux2-Klein-9B-True-v2-int8_convrot.safetensors", "default", 991152863073630, "randomize", 6, 1, "euler_a`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
