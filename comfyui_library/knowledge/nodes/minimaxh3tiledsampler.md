# MiniMaxH3TiledSampler

## 节点类型

`MiniMaxH3TiledSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `noise:NOISE`（1 次）
- `guider:GUIDER`（1 次）
- `sampler:SAMPLER`（1 次）
- `sigmas:SIGMAS`（1 次）
- `latent_image:LATENT`（1 次）
- `bypass_tiling:BOOLEAN`（1 次）
- `tile_axis:COMBO`（1 次）
- `n_tiles:INT`（1 次）
- `tile_overlap:INT`（1 次）
- `max_size_for_no_tile:INT`（1 次）

## 输出

- `分块采样结果:LATENT`（1 次）
- `去噪预测结果:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, "auto", 2, 16, 32, 17, "replicate_last", true, 4, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
