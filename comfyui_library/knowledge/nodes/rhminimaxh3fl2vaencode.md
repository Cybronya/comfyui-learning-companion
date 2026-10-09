# RHMiniMaxH3FL2VAEncode

## 节点类型

`RHMiniMaxH3FL2VAEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `h3_text_encoder:MINIMAX_H3_TEXT_ENCODER`（8 次）
- `h3_vae_bundle:MINIMAX_H3_VAE_BUNDLE`（8 次）
- `target:MINIMAX_H3_TARGET`（8 次）
- `keyframes:MINIMAX_H3_FL_KEYFRAMES`（8 次）
- `prompt:STRING`（8 次）

## 输出

- `conditioning:MINIMAX_H3_CONDITIONING`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[""]`（7 次）
- `["自行生成视频"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
