# RegionalSampler

## 节点类型

`RegionalSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `samples:LATENT`（2 次）
- `base_sampler:KSAMPLER_ADVANCED`（2 次）
- `regional_prompts:REGIONAL_PROMPTS`（2 次）

## 输出

- `LATENT:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[441203147025626, "fixed", 652697203149440, "ignore", 20, 4, 1, 10, true, "ratio between", "AUTO", 0.3]`（1 次）
- `[576957985018381, "fixed", 30, "ignore", 25, 4, 1, 10, true, "ratio between", "AUTO", 0.3]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
