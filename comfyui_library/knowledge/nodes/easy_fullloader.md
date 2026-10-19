# easy fullLoader

## 节点类型

`easy fullLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_override:MODEL`（2 次）
- `clip_override:CLIP`（2 次）
- `vae_override:VAE`（2 次）
- `optional_lora_stack:LORA_STACK`（2 次）
- `optional_controlnet_stack:CONTROL_NET_STACK`（2 次）
- `ckpt_name:COMBO`（2 次）
- `config_name:COMBO`（2 次）
- `vae_name:COMBO`（2 次）
- `clip_skip:INT`（2 次）
- `lora_name:COMBO`（2 次）

## 输出

- `pipe:PIPE_LINE`（2 次）
- `model:MODEL`（2 次）
- `vae:VAE`（2 次）
- `clip:CLIP`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["SDXL_Juggernaut.safetensors", "Default", "Baked VAE", -2, "None", 1, 1, "1280 x 768", 512, 512, "", "none", "comfy", "`（1 次）
- `["juggernautXL_XI.safetensors", "Default", "Baked VAE", -2, "None", 1, 1, "width x height (custom)", 1280, 720, "solo, w`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
