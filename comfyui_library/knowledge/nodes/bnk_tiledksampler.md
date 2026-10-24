# BNK_TiledKSampler

## 节点类型

`BNK_TiledKSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent_image:LATENT`（2 次）

## 输出

- `LATENT:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1055936316635400, "fixed", 1024, 1024, "random", 28, 8, "dpmpp_2m", "karras", 0.15000000000000002]`（1 次）
- `[1055936316635400, "fixed", 1024, 1024, "random", 28, 8, "dpmpp_2m", "karras", 0.2]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
