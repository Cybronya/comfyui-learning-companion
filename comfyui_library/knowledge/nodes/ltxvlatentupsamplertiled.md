# LTXVLatentUpsamplerTiled

## 节点类型

`LTXVLatentUpsamplerTiled`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 16 个 workflow 中。

## 输入

- `samples:LATENT`（16 次）
- `upscale_model:LATENT_UPSCALE_MODEL`（16 次）
- `vae:VAE`（16 次）
- `tile_size:INT`（16 次）
- `overlap:INT`（16 次）
- `max_size_for_no_tile:INT`（16 次）
- `rotate_for_landscape:BOOLEAN`（16 次）
- `debug:BOOLEAN`（16 次）

## 输出

- `LATENT:LATENT`（16 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[11, 6, 22, false, false]`（13 次）
- `[8, 32, 256, false, false]`（2 次）
- `[24, 8, 24, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
