# FluxSamplerParams+

## 节点类型

`FluxSamplerParams+`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（11 次）
- `conditioning:CONDITIONING`（11 次）
- `latent_image:LATENT`（11 次）
- `loras:LORA_PARAMS`（11 次）
- `seed:STRING`（11 次）
- `sampler:STRING`（11 次）
- `scheduler:STRING`（11 次）
- `steps:STRING`（11 次）
- `denoise:STRING`（3 次）

## 输出

- `latent:LATENT`（11 次）
- `params:SAMPLER_PARAMS`（11 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["?,?,?", "dpm_adaptive", "sgm_uniform", "20", "3.5", "1.15", "0.5", "1"]`（4 次）
- `["?,?,?", "dpm_adaptive", "sgm_uniform", "20", "10", "1.15", "0.5", "1"]`（2 次）
- `["?,?,?", "dpm_adaptive", "sgm_uniform", "20", "3.5", "1.15", "0.5", ".7"]`（1 次）
- `["?,?,?", "dpm_adaptive", "sgm_uniform", "20", "3.5", "1.15", "0.5", ".33"]`（1 次）
- `["?,?,?", "dpm_adaptive", "sgm_uniform", "20", "3.5", "1.15", "0.5", ".4"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
