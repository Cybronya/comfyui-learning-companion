# workflow>视频

## 节点类型

`workflow>视频`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `references:MINIMAX_H3_REFERENCES`（1 次）
- `Image Reference image:IMAGE`（1 次）
- `Image Reference 2 image:IMAGE`（1 次）
- `conditioning:MINIMAX_H3_CONDITIONING`（1 次）
- `sampler_config:MINIMAX_H3_SAMPLER_CONFIG`（1 次）
- `model_root:COMBO`（1 次）
- `dtype:COMBO`（1 次）
- `text_encoder_path:COMBO`（1 次）
- `Ref2VA DiT Loader model_root:COMBO`（1 次）

## 输出

- `h3_text_encoder:MINIMAX_H3_TEXT_ENCODER`（1 次）
- `h3_vae_bundle:MINIMAX_H3_VAE_BUNDLE`（1 次）
- `references:MINIMAX_H3_REFERENCES`（1 次）
- `target:MINIMAX_H3_TARGET`（1 次）
- `shape_info:STRING`（1 次）
- `VIDEO:VIDEO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["MiniMax-H3", "auto", "qwen3-vl-32b-int8_convrot.safetensors", "MiniMax-H3", "auto", "MiniMax-H3-Ref2VA-int8_convrot.sa`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
