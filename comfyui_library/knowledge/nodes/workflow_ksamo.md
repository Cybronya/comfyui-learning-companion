# workflow/ksamo

## 节点类型

`workflow/ksamo`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（4 次）
- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）
- `latent_image:LATENT`（4 次）
- `vae:VAE`（4 次）

## 输出

- `LATENT:LATENT`（4 次）
- `IMAGE:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[187619948719748, "randomize", 10, 2, "euler_ancestral", "karras", 1]`（1 次）
- `[211292501379171, "randomize", 8, 1.7, "euler_ancestral", "karras", 1]`（1 次）
- `[688856989964166, "randomize", 10, 2, "euler_ancestral", "karras", 1]`（1 次）
- `[823609115242726, "randomize", 10, 2, "euler_ancestral", "karras", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
