# FYESampler

## 节点类型

`FYESampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipeline:FYEPIPE`（1 次）
- `clip_embeds:FYECLIPEMBED`（1 次）
- `ref_latent:LATENT`（1 次）
- `landmark_features:LMKFEAT`（1 次）

## 输出

- `samples:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[25, 3.5, 326987853747079, "randomize", 24, 4, 1, 1, 1, 1, 1, "DDIMScheduler"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
