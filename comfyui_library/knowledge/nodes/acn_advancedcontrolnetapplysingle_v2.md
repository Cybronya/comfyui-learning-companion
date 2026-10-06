# ACN_AdvancedControlNetApplySingle_v2

## 节点类型

`ACN_AdvancedControlNetApplySingle_v2`

## 分类

Conditioning

## 作用

ControlNet 控制类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `conditioning:CONDITIONING`（2 次）
- `control_net:CONTROL_NET`（2 次）
- `image:IMAGE`（2 次）
- `mask_optional:MASK`（2 次）
- `timestep_kf:TIMESTEP_KEYFRAME`（2 次）
- `latent_kf_override:LATENT_KEYFRAME`（2 次）
- `weights_override:CONTROL_NET_WEIGHTS`（2 次）
- `vae_optional:VAE`（2 次）

## 输出

- `CONDITIONING:CONDITIONING`（2 次）
- `model_opt:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.6000000000000001, 0, 0.7000000000000002]`（1 次）
- `[0.6, 0, 0.6000000000000001]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
