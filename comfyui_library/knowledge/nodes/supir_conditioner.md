# SUPIR_conditioner

## 节点类型

`SUPIR_conditioner`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `SUPIR_model:SUPIRMODEL`（1 次）
- `latents:LATENT`（1 次）
- `captions:STRING`（1 次）

## 输出

- `positive:SUPIR_cond_pos`（1 次）
- `negative:SUPIR_cond_neg`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["high quality, detailed, photograph", "bad quality, blurry, messy", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
