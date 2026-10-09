# MiniMaxH3DirectorRefine

## 节点类型

`MiniMaxH3DirectorRefine`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `refine_model:MODEL`（1 次）
- `sigmas:SIGMAS`（1 次）
- `upscale_model:UPSCALE_MODEL`（1 次）
- `mode:COMBO`（1 次）
- `upscale_method:COMBO`（1 次）
- `latent_upscale_model:COMBO`（1 次）
- `sampler:COMBO`（1 次）
- `passes:INT`（1 次）
- `seed_mode:COMBO`（1 次）
- `aspect_ratio:COMBO`（1 次）

## 输出

- `refine:MMX_DIR_REFINE`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["refine", "h3_latent", "", "euler", 1, "inherit", "跟随导演台", 1, 1280, 720, true, false, false, false, 2, 128]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
