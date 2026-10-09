# RHMiniMaxH3DecodeAV

## 节点类型

`RHMiniMaxH3DecodeAV`

## 分类

Decoding

## 作用

解码类节点：把编码数据还原（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 21 个 workflow 中。

## 输入

- `h3_vae_bundle:MINIMAX_H3_VAE_BUNDLE`（21 次）
- `sampled_av_latent:MINIMAX_H3_AV_LATENT`（21 次）

## 输出

- `frames:IMAGE`（21 次）
- `audio:AUDIO`（21 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[]`（18 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
