# Lynx_KSampler

## 节点类型

`Lynx_KSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:Lynx_MODEL`（1 次）
- `conds:Lynx_COND`（1 次）
- `lora:COMBO`（1 次）
- `seed:INT`（1 次）
- `steps:INT`（1 次）
- `num_frames:INT`（1 次）
- `cfg:FLOAT`（1 次）
- `cfg_i:FLOAT`（1 次）
- `ip_scale:FLOAT`（1 次）
- `ref_scale:FLOAT`（1 次）

## 输出

- `LATENT:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["lightx2v_I2V_14B_480p_cfg_step_distill_rank128_bf16.safetensors", 363082813, "fixed", 8, 121, 1, 2, 1, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
