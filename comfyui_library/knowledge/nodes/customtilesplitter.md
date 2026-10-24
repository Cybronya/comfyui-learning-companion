# CustomTileSplitter

## 节点类型

`CustomTileSplitter`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `latent:LATENT`（1 次）
- `tile_size:INT`（1 次）
- `overlap:INT`（1 次）

## 输出

- `tiles_image_batch:IMAGE`（1 次）
- `tiles_image_list:IMAGE`（1 次）
- `tiles_latent_batch:LATENT`（1 次）
- `tiles_latent_list:LATENT`（1 次）
- `tile_config:TILE_CONFIG`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1152, 64]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
