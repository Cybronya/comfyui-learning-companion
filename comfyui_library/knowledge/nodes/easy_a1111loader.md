# easy a1111Loader

## 节点类型

`easy a1111Loader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `optional_lora_stack:LORA_STACK`（1 次）
- `optional_controlnet_stack:CONTROL_NET_STACK`（1 次）
- `ckpt_name:COMBO`（1 次）
- `vae_name:COMBO`（1 次）
- `clip_skip:INT`（1 次）
- `lora_name:COMBO`（1 次）
- `lora_model_strength:FLOAT`（1 次）
- `lora_clip_strength:FLOAT`（1 次）
- `resolution:COMBO`（1 次）
- `empty_latent_width:INT`（1 次）

## 输出

- `pipe:PIPE_LINE`（1 次）
- `model:MODEL`（1 次）
- `vae:VAE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["SD1.5 human\\majicMIX realistic 麦橘写实_v7 亚洲男性微调.safetensors", "vae-ft-mse-840000-ema-pruned.ckpt", -2, "None", 1, 1, "5`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
