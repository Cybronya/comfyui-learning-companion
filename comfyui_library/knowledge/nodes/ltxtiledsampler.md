# LTXTiledSampler

## 节点类型

`LTXTiledSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `noise:NOISE`（2 次）
- `guider:GUIDER`（2 次）
- `sampler:SAMPLER`（2 次）
- `sigmas:SIGMAS`（2 次）
- `latent_image:LATENT`（2 次）
- `bypass_tiling:BOOLEAN`（2 次）
- `tile_axis:COMBO`（2 次）
- `n_tiles:INT`（2 次）
- `tile_overlap:INT`（2 次）
- `max_size_for_no_tile:INT`（2 次）

## 输出

- `output:LATENT`（2 次）
- `denoised_output:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, "auto", 2, 8, 24, "passthrough", "first", false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
