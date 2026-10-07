# LotusSampler

## 节点类型

`LotusSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `lotus_unet:LOTUSUNET`（1 次）
- `samples:LATENT`（1 次）
- `seed:INT`（1 次）
- `per_batch:INT`（1 次）
- `keep_model_loaded:BOOLEAN`（1 次）

## 输出

- `samples:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[738945725, "randomize", 4, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
