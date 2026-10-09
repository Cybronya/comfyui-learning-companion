# FeiHouEasyH3RHRemixLoader

## 节点类型

`FeiHouEasyH3RHRemixLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `first_pass_lora_stack:FEIHOU_MERGE_LORA_STACK`（3 次）
- `second_pass_lora_stack:FEIHOU_MERGE_LORA_STACK`（3 次）
- `remix_model:COMBO`（3 次）
- `text_encoder:COMBO`（3 次）
- `video_vae:COMBO`（3 次）
- `audio_vae:COMBO`（3 次）
- `second_sampling_model:COMBO`（3 次）

## 输出

- `h3_bundle:MINIMAX_H3_BUNDLE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["FeiHou_MiniMax-H3_Remix_HSA_v0.7.safetensors", "qwen3vl_32b_minimax_h3_int8_convrot.safetensors", "minimax_h3_video_va`（2 次）
- `["FeiHou_MiniMax-H3_Remix_HSA_turbo_v0.8_int8_convrotHQ.safetensors", "qwen3vl_32b_minimax_h3_bf16.safetensors", "minima`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
