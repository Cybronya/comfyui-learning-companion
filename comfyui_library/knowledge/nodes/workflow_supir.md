# workflow/supir解码编码

## 节点类型

`workflow/supir解码编码`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `SUPIR_VAE:SUPIRVAE`（1 次）
- `图像:IMAGE`（1 次）
- `SUPIR_decode SUPIR_VAE:SUPIRVAE`（1 次）
- `Latent:LATENT`（1 次）
- `编码分块尺寸:INT`（1 次）
- `解码分块尺寸:INT`（1 次）
- `SUPIR_decode decoder_tile_size:INT`（1 次）
- `SUPIR_encode encoder_tile_size:INT`（1 次）

## 输出

- `Latent:LATENT`（1 次）
- `image:IMAGE`（1 次）
- `SUPIR_encode Latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, "auto", true, true, "auto", 512, 512, 512, 512]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
