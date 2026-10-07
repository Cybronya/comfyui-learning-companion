# ClownsharKSampler_Beta

## 节点类型

`ClownsharKSampler_Beta`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent_image:LATENT`（2 次）
- `sigmas:SIGMAS`（2 次）
- `guides:GUIDES`（2 次）
- `options:OPTIONS`（2 次）
- `eta:FLOAT`（2 次）
- `sampler_name:COMBO`（2 次）
- `scheduler:COMBO`（2 次）

## 输出

- `output:LATENT`（2 次）
- `denoised:LATENT`（2 次）
- `options:OPTIONS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.5, "exponential/res_3s", "bong_tangent", 10, -1, 0.6000000000000001, 1.0000000000000002, 1118927387579896, "randomize`（1 次）
- `[0.5, "exponential/res_3s", "bong_tangent", 6, -1, 1, 1.0000000000000002, 718876291325225, "fixed", "standard", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
