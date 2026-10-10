# MiniMaxH3ChainContext

## 节点类型

`MiniMaxH3ChainContext`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `state:H3_CHAIN_STATE`（1 次）
- `conditioning:CONDITIONING`（1 次）
- `vae:VAE`（1 次）
- `latent:LATENT`（1 次）
- `audio_vae:VAE`（1 次）
- `model:MODEL`（1 次）
- `drift_sigmas:SIGMAS`（1 次）
- `lip_sync_voice:AUDIO`（1 次）

## 输出

- `conditioning:CONDITIONING`（1 次）
- `trim_frames:INT`（1 次）
- `is_continuation:BOOLEAN`（1 次）
- `latent:LATENT`（1 次）
- `model:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
